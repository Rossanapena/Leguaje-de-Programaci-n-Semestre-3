public class Obra {

    protected String titulo;
    protected String autor;
    protected String periodo;
    protected double valor;

    public Obra(String titulo, String autor, String periodo, double valor) {
        this.titulo = titulo;
        this.autor = autor;
        this.periodo = periodo;
        this.valor = valor;
    }

    public void mostrarInfo() {
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Periodo: " + periodo);
        System.out.println("Valor: " + valor);
    }
}
