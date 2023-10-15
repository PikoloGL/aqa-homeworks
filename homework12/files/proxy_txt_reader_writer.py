from interfaces.iwrite import Write
from interfaces.iread import Read
from txt_writer import TxtWriter
from txt_reader import TxtReader


class ProxyTxtRW(Read):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, text):
        current_content = self.__real_reader.read()
        if text != current_content:
            self.__real_writer.write(text)
            self.__result = text
            self.__is_actual = True


if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer_writer = TxtWriter('my_file.txt')
    proxy = ProxyTxtRW(reader_reader, writer_writer)
    print(proxy.read())  # Read file
    # Write new content through the proxy
    new_content = "This is new content written through the proxy."
    proxy.write(new_content)
    # Read and print the updated file content
    updated_content = proxy.read()
    print(updated_content)
