import os
import ctypes
import struct

libc = ctypes.CDLL("libc.so.6")

class IOVec(ctypes.Structure):
    _fields_ = [
        ("iov_base", ctypes.c_void_p),
        ("iov_len", ctypes.c_size_t)
    ]


process_vm_readv = libc.process_vm_readv
process_vm_readv.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(IOVec),
    ctypes.c_ulong,
    ctypes.POINTER(IOVec),
    ctypes.c_ulong,
    ctypes.c_ulong
]
process_vm_readv.restype = ctypes.c_ssize_t


class PymemLinux:
    def __init__(self, pid):
        self.process_id = pid

        if os.getuid() != 0:
            raise OSError("Pymem requires root privileges")

    def module_base(self, name: str) -> int:
        if not self.process_id:
            raise Exception("You must open a process before calling this method")

        for line in open(f"/proc/{self.process_id}/maps"):
            if name in line:
                return int(line.split("-")[0], 16)
        raise Exception("Module not found")

    def process_died(self) -> bool:
        try:
            os.kill(self.process_id, 0)
        except OSError:
            return True
        else:
            return False

    def read_bytes(self, address: int, byte: int):
        """Read the given amount of bytes from `address`"""
        if not self.process_id:
            raise Exception("You must open a process before calling this method")

        buff = ctypes.create_string_buffer(byte)
        io_dst = IOVec(ctypes.cast(ctypes.byref(buff), ctypes.c_void_p), byte)
        io_src = IOVec(ctypes.c_void_p(address), byte)

        if process_vm_readv(self.process_id, ctypes.byref(io_dst), 1, ctypes.byref(io_src), 1, 0) == -1:
            raise OSError(ctypes.get_errno())

        return buff.raw

    def read_vec3(self, address: int) -> dict[str, float]:
        bytes = self.read_bytes(address, struct.calcsize("3f"))
        bytes = struct.unpack("3f", bytes)
        return {"x": bytes[0], "y": bytes[1], "z": bytes[2]}

    def read_vec2(self, address: int) -> dict[str, float]:
        bytes = self.read_bytes(address, struct.calcsize("2f"))
        bytes = struct.unpack("2f", bytes)
        return {"x": bytes[0], "y": bytes[1]}

    def read_bool(self, address: int) -> bool:
        bytes = self.read_bytes(address, struct.calcsize("?"))
        bytes = struct.unpack("?", bytes)[0]
        return bytes

    def read_char(self, address: int) -> str:
        bytes = self.read_bytes(address, struct.calcsize("c"))
        bytes = struct.unpack("<c", bytes)[0]
        bytes = bytes.decode()
        return bytes

    def read_uchar(self, address: int) -> str:
        bytes = self.read_bytes(address, struct.calcsize("B"))
        bytes = struct.unpack("<B", bytes)[0]
        return bytes

    def read_short(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("h"))
        bytes = struct.unpack("<h", bytes)[0]
        return bytes

    def read_ushort(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("H"))
        bytes = struct.unpack("<H", bytes)[0]
        return bytes

    def read_int(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("i"))
        bytes = struct.unpack("<i", bytes)[0]
        return bytes

    def read_uint(self, address: int) -> int:
        raw = self.read_bytes(address, struct.calcsize("I"))
        raw = struct.unpack("<I", raw)[0]
        return raw

    def read_float(self, address: int) -> float:
        bytes = self.read_bytes(address, struct.calcsize("f"))
        bytes = struct.unpack("<f", bytes)[0]
        return bytes

    def read_long(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("l"))
        bytes = struct.unpack("<l", bytes)[0]
        return bytes

    def read_ulong(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("L"))
        bytes = struct.unpack("<L", bytes)[0]
        return bytes

    def read_longlong(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("q"))
        bytes = struct.unpack("<q", bytes)[0]
        return bytes

    def read_ulonglong(self, address: int) -> int:
        bytes = self.read_bytes(address, struct.calcsize("Q"))
        bytes = struct.unpack("<Q", bytes)[0]
        return bytes

    read_pointer_64bit = read_ulonglong

    def read_double(self, address: int) -> float:
        bytes = self.read_bytes(address, struct.calcsize("d"))
        bytes = struct.unpack("<d", bytes)[0]
        return bytes

    def read_string(self, address: int, byte=52) -> str:
        buff = self.read_bytes(address + 0x14, byte)
        i = buff.find(b"\x00\x00")  # find null terminator
        if i != -1:
            buff = buff[:i + 1]
        try:
            return buff.decode('utf-16')
        except UnicodeDecodeError:
            return buff.replace(b"\x00", b"").decode("utf-8")
