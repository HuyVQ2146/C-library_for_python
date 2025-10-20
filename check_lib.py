import ctypes

# Trong terminal, cd "PATH" sang directory chứa cả .py, .cpp
# g++ -shared -o cpp_lib.dll cpp_lib.cpp -static 
cpp_lib = ctypes.CDLL("C:\\Users\\VU QUANG HUY\\OneDrive\\Desktop\\code\\C++_Learning\\ctypes\\cpp_lib.dll")

print("Hello world func:")
cpp_lib.hello()

print(f"Add num func: {cpp_lib.add_num(4, 17)}")
