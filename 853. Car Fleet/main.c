typedef struct Car {
    int position;
    int speed;
} Car;

int comparator(const void* a, const void* b) {
    const Car* carA = a;
    const Car* carB = b;
    return carA->position - carB->position;
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    Car* cars = malloc(positionSize * sizeof(Car));

    for (int i = 0; i < positionSize; i++) {
        cars[i] = (Car){position[i], speed[i]};
    }

    qsort(cars, positionSize, sizeof(Car), comparator);

    float timeToTargetOfSlowestCar = 0;
    int fleets = 0;
    
    for (int i = positionSize-1; i >= 0; i--) {
        Car car = cars[i];
        float timeToTarget = (target - car.position) / (float) car.speed;
        
        if (timeToTarget > timeToTargetOfSlowestCar) {
            fleets += 1;
            timeToTargetOfSlowestCar = timeToTarget;
        }
    }
    free(cars);

    return fleets;
}