public class Car implements CarbonFootprint {

    private String model;
    private double fuelConsumption;

    public Car(String model, double fuelConsumption) {
        this.model = model;
        this.fuelConsumption = fuelConsumption;
    }

    public String getModel() {
        return model;
    }

    public double getFuelConsumption() {
        return fuelConsumption;
    }

    @Override
    public double getCarbonFootprint() {
        return fuelConsumption * 2.3;
    }

    @Override
    public String toString() {
        return "Car: " + model +
               " | Carbon Footprint: " + getCarbonFootprint();
    }
}
