import React from "react";
import "../styles/auth.css"

function SignUp(){
    return (
        <div className="auth-container">
        <div className="auth-box">
            <h2>Crear una Cuenta</h2>
            <form id="registroForm">
                <div className="input-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" placeholder="Tu nombre" required/>
                </div>
                <div className="input-group">
                    <label for="apellido">Apellido:</label>
                    <input type="text" id="apellido" name="apellido" placeholder="Tu apellido" required/>
                </div>
                <div className="input-group">
                    <label for="email">Correo Electrónico:</label>
                    <input type="email" id="email" name="correo" placeholder="tu@ejemplo.com" required/>
                </div>
                <div className="input-group">
                    <label for="password">Contraseña:</label>
                    <input type="password" id="password" name="contrasena" placeholder="********" required/>
                </div>
                <div className="input-group">
                    <label for="confirm_password">Confirmar Contraseña:</label>
                    <input type="password" id="confirm_password" name="confirm_contrasena" placeholder="********" required/>
                </div>
                <div className="input-group">
                    <label for="user_type">Tipo de Usuario:</label>
                    <select id="user_type" name="tipo" required>
                        <option value="">Selecciona un tipo</option>
                        <option value="1">Alumno</option>
                        <option value="2">Maestro</option>
                    </select>
                </div>
                
                <div className="input-group" id="curp_group" style={{display: "block"}}>
                    <label for="curp">CURP:</label>
                    <input type="text" id="curp" name="curp" placeholder="Tu CURP"/>
                </div>

                <button type="submit" className="btn">Registrarse</button>
                <div className="links">
                    <p>¿Ya tienes cuenta? <a href="login.html">Inicia sesión aquí</a></p>
                </div>
            </form>
        </div>
    </div>
    )
}

export default SignUp;