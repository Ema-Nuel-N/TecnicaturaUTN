
package domain;

import java.util.Date;

public class Cliente extends Persona{

    private int idCliente;
    private static int contadorClientes;
    private Date fechaRegistro;
    private boolean vip;
    
    public Cliente(String nombre,boolean vip,char genero, int edad, String direccion, Date fecha){
        super(nombre, genero, edad, direccion);
        this.vip = vip;
        this.idCliente = ++contadorClientes;
        this.fechaRegistro = fecha;
    }

    public int getIdCliente() {
        return this.idCliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{idCliente = ").append(idCliente);
        sb.append(", fechaRegistro = ").append(fechaRegistro);
        sb.append(", vip = ").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }


    
    
    
}
