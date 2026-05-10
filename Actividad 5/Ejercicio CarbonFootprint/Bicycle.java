public class Bicycle implements CarbonFootprint {

    private String type;
    private double distance;

    public Bicycle(String type, double distance) {
        this.type = type;
        this.distance = distance;
    }

    public String getType() {
        return type;
    }

    public double getDistance() {
        return distance;
    }

    @Override
    public double getCarbonFootprint() {
        return distance * 0.05;
    }

    @Override
    public String toString() {
        return "Bicycle: " + type +
               " | Carbon Footprint: " + getCarbonFootprint();
    }
}
