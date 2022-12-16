def get_actions_v1(kms):
    if kms > 300000:
        return 'sell vehicle for scrap metal'
    return None


def get_actions_v2(kms, vehicle_type):
    if kms > 300000:
        return 'sell vehicle for scrap metal'
    if vehicle_type == 'car':
        return 'sell car to car dealer'
    if vehicle_type == 'truck':
        return 'sell truck to truck dealer'
    return None
