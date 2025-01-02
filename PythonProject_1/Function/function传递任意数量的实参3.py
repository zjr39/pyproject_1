def make_car(manufacturer,model,**car_info):
    car_info['manufacturer']=manufacturer           #要用引号
    car_info['model']=model
    return car_info

car=make_car('subaru','outback',color='blue',tow_packaage=True)           #不用引号
print(car)
