from tkinter import *

raiz=Tk()
raiz.title("Maquina Expendedora")
raiz.resizable(False,True)
raiz.config(bg="white")
raiz.iconbitmap("ARB.ico")

miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
Label(miFrame, text="Ingrese tipo de usuario : ", fg="black" , font=(18)).place(x=20,y=20)
miFrame.config(bg="light blue")

botonAdministrador = Button(raiz,text=" Administrador ")
botonAdministrador.place(x=20,y=60)

minombre=StringVar()
cuadro = Entry(miFrame, textvariable=minombre)
cuadro.grid(row=0 ,column=1 , padx=10 ,pady=0)
cuadro

cuadro.place(x=20,y=60)

def codigoAdministrador():
    minombre.set("Alvaro")

botonCliente = Button(raiz,text="   Cliente   ",command=codigoAdministrador)
botonCliente.place(x=130,y=60)

raiz.mainloop()
package Archivos;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class EscribeArchivo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String nombreArchivo = "texto.txt";
		
		try {
			
			FileWriter fw = new FileWriter(nombreArchivo);
			BufferedWriter bw = new BufferedWriter(fw);
			
			bw.write("Que facilito es...");
			bw.newLine();
			bw.write("es escribir archivos!");
			
			bw.close();
			
			System.out.println("Reto cumplido");
			
	
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

package Archivos;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class EscribeArchivo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String nombreArchivo = "texto.txt";
		
		try {
			
			FileWriter fw = new FileWriter(nombreArchivo);
			BufferedWriter bw = new BufferedWriter(fw);
			
			bw.write("Que facilito es...");
			bw.newLine();
			bw.write("es escribir archivos!");
			
			bw.close();
			
			System.out.println("Reto cumplido");	
	
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
----------------------
private void jBLeerActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // TODO add your handling code here:
        
        String nombre = JTNombreArchivo.getText();
        
        try {
            FileReader fr = new FileReader(nombre);
            
            BufferedReader br = new BufferedReader(fr);
            
            String line="";
            String tota="";
            while((line=br.readLine())!=null){
                tota+=line+"\n"; // por cada linea leida agregamos un salto de linea
            }

            jTextArchivo.setText(tota);
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(JFArchivo.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(JFArchivo.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }                                      

    private void jBEscribirActionPerformed(java.awt.event.ActionEvent evt) {                                           
        // TODO add your handling code here:
        
        String texto = JTNombreArchivo.getText();
        
        try {
            FileWriter fw = new FileWriter(texto);
            BufferedWriter bw = new BufferedWriter(fw);
            
            bw.write(jTextArchivo.getText());
            
            bw.close();
            
           
        } catch (IOException ex) {
            Logger.getLogger(JFArchivo.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }  
