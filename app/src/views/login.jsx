import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import "../styles/auth.css"

function Login() {
    const navigate = useNavigate();
    const [loginData, setLoginData] = useState({ correo: "", contrasena: "" });

    const changeData = async (e) => {
        const {name, value} = e.target;
        setLoginData(prev => ({...prev, [name]: value}));
    }

    const fetchLogin = async (e) => {
        try {
            e.preventDefault();
            const peticion = await fetch("http://localhost:8000/iniciar-sesion", { method: "POST", headers:{ 
                 "Content-Type": "application/json"
            }, 
            body: JSON.stringify(loginData) });

            const respuesta = await peticion.json();
            console.log(respuesta)

            if(!respuesta.estatus) return alert("Credenciales incorrectas");
            alert(respuesta.result.message);
            navigate(`/${respuesta.result.tipo_usuario}/`);
            return;
        } catch (error) {
            console.error("Ha sucedido un error: ", error);
            alert("Favor de intentarlo de nuevo más tarde");
        }
    }

    return (
    <div className="auth-container">
        <div className="auth-box">
            <h2>Iniciar Sesión</h2>
            <form onSubmit={(e)=>fetchLogin(e)}>
                <div className="input-group">
                    <label htmlFor="email">Correo Electrónico:</label>
                    <input type="email" id="email" 
                    name="correo" placeholder="tu@ejemplo.com" 
                    onChange={ (e) => changeData(e) } required/>
                </div>
                <div className="input-group">
                    <label htmlFor="password">Contraseña:</label>
                    <input type="password" id="password" name="contrasena" 
                    placeholder="********" onChange={ (e) => changeData(e) } required/>
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