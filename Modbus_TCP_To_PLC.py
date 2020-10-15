import modbus_tk

#modbus_tk.defines.READ_COILS = 0x01
#modbus_tk.defines.READ_DISCRETE_INPUTS = 0x02
#modbus_tk.defines.READ_HOLDING_REGISTERS = 0x03
#modbus_tk.defines.READ_INPUT_REGISTERS = 0x04
#modbus_tk.defines.WRITE_SINGLE_COIL = 0x05
#modbus_tk.defines.WRITE_SINGLE_REGISTER = 0x06

master = modbus_tk.modbus_tcp.TcpMaster("0.0.0.0")
a = master.execute(1,modbus_tk.defines.WRITE_SINGLE_REGISTER,0x1068,0x01,0x00)
for x in a:
    print(x)
