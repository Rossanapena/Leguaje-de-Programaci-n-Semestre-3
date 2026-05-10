import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class FileManager {

    public static void saveToJson(List<CarbonFootprint> objects) {

        try (FileWriter writer = new FileWriter("data/carbon_data.json")) {

            writer.write("[\n");

            for (int i = 0; i < objects.size(); i++) {

                CarbonFootprint object = objects.get(i);

                writer.write("  {\n");
                writer.write("    \"description\": \"" + object.toString() + "\",\n");
                writer.write("    \"carbonFootprint\": " + object.getCarbonFootprint() + "\n");
                writer.write("  }");

                if (i < objects.size() - 1) {
                    writer.write(",");
                }

                writer.write("\n");
            }

            writer.write("]");

            System.out.println("Data saved successfully in JSON file.");

        } catch (IOException e) {

            System.out.println("Error saving file: " + e.getMessage());
        }
    }
}
