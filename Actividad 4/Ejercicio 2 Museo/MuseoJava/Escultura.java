public class Escultura extends Obra {

    private String material;

    public Escultura(String titulo, String autor, String periodo, double valor, String material) {
        super(titulo, autor, periodo, valor);
        this.material = material;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Material: " + material);
    }
}
