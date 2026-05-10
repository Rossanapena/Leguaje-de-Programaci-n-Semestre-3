import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

        Building building = new Building("Office Building", 500);

        Car car = new Car("Toyota Corolla", 120);

        Bicycle bicycle = new Bicycle("Mountain Bike", 50);

        ArrayList<CarbonFootprint> objects = new ArrayList<>();

        objects.add(building);
        objects.add(car);
        objects.add(bicycle);

        for (CarbonFootprint object : objects) {

            System.out.println(object.toString());
        }

        FileManager.saveToJson(objects);
    }
}
