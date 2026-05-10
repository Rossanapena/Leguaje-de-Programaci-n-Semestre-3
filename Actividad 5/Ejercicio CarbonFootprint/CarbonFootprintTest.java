public class CarbonFootprintTest {

    public static void main(String[] args) {

        Building building = new Building("Test Building", 100);

        Car car = new Car("Test Car", 50);

        Bicycle bicycle = new Bicycle("Test Bicycle", 20);

        System.out.println("=== UNIT TESTS ===");

        System.out.println(
            "Building Test: " +
            (building.getCarbonFootprint() == 50.0 ? "PASSED" : "FAILED")
        );

        System.out.println(
            "Car Test: " +
            (Math.abs(car.getCarbonFootprint() - 115.0) < 0.01 ? "PASSED" : "FAILED")
        );

        System.out.println(
            "Bicycle Test: " +
            (bicycle.getCarbonFootprint() == 1.0 ? "PASSED" : "FAILED")
        );
    }
}
