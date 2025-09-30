import supervisor
import usb_hid

supervisor.set_usb_identification(product="USB Mouse", manufacturer="Goldenboy Industries")

usb_hid.enable((usb_hid.Device.MOUSE,), boot_device=1)
