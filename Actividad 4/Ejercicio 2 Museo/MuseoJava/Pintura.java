public class Pintura extends Obra {

    private String tecnica;

    public Pintura(String titulo, String autor, String periodo, double valor, String tecnica) {
        super(titulo, autor, periodo, valor);
        this.tecnica = tecnica;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Técnica: " + tecnica);
    }
}
