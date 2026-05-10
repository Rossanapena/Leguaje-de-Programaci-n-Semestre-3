public class Building implements CarbonFootprint {

    private String name;
    private double electricityConsumption;

    public Building(String name, double electricityConsumption) {
        this.name = name;
        this.electricityConsumption = electricityConsumption;
    }

    public String getName() {
        return name;
    }

    public double getElectricityConsumption() {
        return electricityConsumption;
    }

    @Override
    public double getCarbonFootprint() {
        return electricityConsumption * 0.5;
    }

    @Override
    public String toString() {
        return "Building: " + name +
               " | Carbon Footprint: " + getCarbonFootprint();
    }
}
