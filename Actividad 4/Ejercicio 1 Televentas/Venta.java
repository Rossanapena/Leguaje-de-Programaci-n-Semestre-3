public class Venta {

    private Cliente cliente;
    private Producto producto;
    private int cantidad;
    private Pago pago;

    public Venta(Cliente cliente, Producto producto, int cantidad, Pago pago) {
        this.cliente = cliente;
        this.producto = producto;
        this.cantidad = cantidad;
        this.pago = pago;
    }

    public double calcularTotal() {
        return producto.getPrecio() * cantidad;
    }

    public void procesarVenta() {
        double total = calcularTotal();
        pago.procesarPago(total);

        System.out.println("Cliente: " + cliente.getNombre());
        System.out.println("Producto: " + producto.getNombre());
        System.out.println("Cantidad: " + cantidad);
        System.out.println("Total: " + total);
    }
}
