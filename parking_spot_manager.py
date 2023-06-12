class parking_spot:
    """
    주차장 정보를 저장하는 클래스

    name : 주차장 이름 (str)
    city : 주자창이 있는 시도 (str)
    district : 주차장이 있는 시군구 (str)
    ptype : 주차장 유형 (str)
    longitude : 경도 (float)
    latitude : 위도 (float)
    """
    #constructor(생성자)
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {}
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)
    
    #get method
    def get(self, keyword = 'name'):
        return self.__item[keyword]

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list: list):
    """
    문자열 리스트를 parking_spot 클래스 객체의 리스트로 변환
    """
    list = []
    for parking in str_list:
        _, name, city, district, ptype, longitude, latitude = parking.split(',')
        list.append(parking_spot(name, city, district, ptype, longitude, latitude))

    return list

def print_spots(spots: list):
    """
    주차장 정보 출력
    """
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)

def filter_by_name(spots: list, name: str):
    """
    이름으로 parking_spot 클래스 객체의 리스트 필터링
    """
    return [spot for spot in spots if name in spot.get('name')]

def filter_by_city(spots: list, city: str):
    """
    시도로 parking_spot 클래스 객체의 리스트 필터링
    """
    return [spot for spot in spots if city in spot.get('city')]

def filter_by_district(spots: list, district: str):
    """
    시군구로 parking_spot 클래스 객체의 리스트 필터링
    """
    return [spot for spot in spots if district in spot.get('district')]

def filter_by_ptype(spots: list, ptype: str):
    """
    주차장 유형으로 parking_spot 클래스 객체의 리스트 필터링
    """
    return [spot for spot in spots if ptype in spot.get('ptype')]

def filter_by_location(spots: list, locations: tuple):
    """
    최대, 최소 위도, 경도 범위로 parking_spot 클래스 객체의 리스트 필터링
    """
    min_lat, max_lat, min_long, max_long = locations
    return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_long < spot.get('longitude') < max_long]

def sort_by_keyword(spots: list, keyword: str):
    """
    keyword로 parking_spot 클래스 객체의 리스트를 정렬하여 새로운 리스트로 정렬
    """
    return sorted(spots, key = lambda spot: spot.get(keyword))



# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    #import file_manager
    #str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    #spots = str_list_to_class_list(str_list)
    #print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)