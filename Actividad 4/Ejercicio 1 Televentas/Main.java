public class Main {

    public static void main(String[] args) {

        Cliente cliente = new Cliente("Ana");
        Producto producto = new Producto("Laptop", 2000);

        Pago pago = new PagoTarjeta();

        Venta venta = new Venta(cliente, producto, 2, pago);

        venta.procesarVenta();
    }
}
