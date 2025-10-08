class Hinh_chu_nhat:
    def __init__( self, chieu_dai= 0, chieu_rong= 0):
        self.chieu_dai= chieu_dai
        self.chieu_rong= chieu_rong
    def nhap_do_dai( self):
        self.chieu_dai= float( input(" Nhập chiều dài của hình chữ nhật: "))
        self.chieu_rong= float( input(" Nhập chiều rộng của hình chữ nhật: "))
    def tinh_chu_vi( self):
        return ( self.chieu_dai+ self.chieu_rong) *2
    def tinh_dien_tich( self):
        return self.chieu_dai* self.chieu_rong
    def display( self):
        print(" Chiều dài của hình chữ nhật: ", self.chieu_dai)
        print(" Chiều rộng của hình chữ nhật: ", self.chieu_rong)
        print(" Chu vi của hình chữ nhật: ", self.tinh_chu_vi())
        print(" Diện tích của hình chữ nhật: ", self.tinh_dien_tich())
hcn= Hinh_chu_nhat()
hcn.nhap_do_dai()
hcn.tinh_chu_vi()
hcn.tinh_dien_tich()
hcn.display()