class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        answer = 0
        car_info = list(zip(position, speed))
        car_info.sort(key=lambda x:x[0], reverse=True)
        
        max_step = float("-inf")
        for car_position, car_speed in car_info:
            car_step = (target-car_position) / car_speed
            if max_step < car_step:
                max_step = car_step
                answer += 1
        
        return answer