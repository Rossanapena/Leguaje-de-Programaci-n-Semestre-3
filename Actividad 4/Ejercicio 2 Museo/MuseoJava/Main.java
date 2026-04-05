public class Main {

    public static void main(String[] args) {

        Pintura pintura = new Pintura(
                "La Mona Lisa",
                "Leonardo da Vinci",
                "Renacimiento",
                1000000,
                "Óleo"
        );

        Escultura escultura = new Escultura(
                "El Pensador",
                "Rodin",
                "Moderno",
                500000,
                "Bronce"
        );

        pintura.mostrarInfo();
        System.out.println("------------------");
        escultura.mostrarInfo();
    }
}
