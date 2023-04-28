def get_actions(kms, vehicle_type):
    if vehicle_type == 'car':
        return 'sell car to car dealer'
    elif vehicle_type == 'truck':
        return 'sell truck to truck dealer'
    else:
        return None
