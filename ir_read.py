from pywinusb import hid

def irRead(data):
    print(data)
    
#    if data[2] > 0:
#        print(f'Нажата кнопка {data[2]} ...')
    return None
    
ir = hid.HidDeviceFilter(vendor_id = 0x1130, product_id = 0xcc00).get_devices()[0]
ir.open()
ir.set_raw_data_handler(irRead)
