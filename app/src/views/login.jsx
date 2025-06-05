import React from 'react';
import { Link } from "react-router-dom";
import "../styles/auth.css"

function Login() {
    return (
    <div class="auth-container">
        <div className="auth-box">
            <h2>Iniciar Sesión</h2>
            <form>
                <div className="input-group">
                    <label for="email">Correo Electrónico:</label>
                    <input type="email" id="email" name="correo" placeholder="tu@ejemplo.com" required/>
                </div>
                <div className="input-group">
                    <label for="password">Contraseña:</label>
                    <input type="password" id="password" name="contrasena" placeholder="********" required/>
                </div>
                <button type="submit" className="btn">Entrar</button>
                <div className="links">
                    <p>¿No tienes cuenta? <Link to="/sign-up">Regístrate aquí</Link></p>
                </div>
            </form>
        </div>
    </div>
    )
}

export default Login;