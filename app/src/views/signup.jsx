import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/auth.css"

function SignUp(){
    const navigate = useNavigate();
    const [signUpData, setSignUpData] = useState({ nombre: "", apellidos:"", correo:"", 
        contrasena: "", confirmar_contrasena: "", tipo: "1", curp: "" });

    const changeData = async (e) => {
        const {name, value} = e.target;
        setSignUpData(prev => ({ ...prev, [name]:value }));
    }

    const fetchSignUp = async (e) => {
        e.preventDefault();
        try {
            const peticion = await fetch("http://localhost:8000/crear_usuario", { method: "POST", headers:{ 
                 "Content-Type": "application/json"
            }, 
            body: JSON.stringify(signUpData) });
            const resultado = await peticion.json();
            console.log(resultado)
            if(!resultado.estatus) return alert("Ya existe un usuario con esas credenciales");
            alert("Se ha creado su cuenta de manera exitosa");
            return navigate("/iniciar-sesion")
        } catch (error) {
            console.error("Ha ocurrido un erorr: ", error);
            return alert("Favor de intentarlo de nuevo más tarde");
        }
    }

    return (
        <div className="auth-container">
        <div className="auth-box">
            <h2>Crear una Cuenta</h2>
            <form id="registroForm" onSubmit={(e) => fetchSignUp(e)}>
                <div className="input-group">
                    <label htmlFor="nombre">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" 
                    onChange={(e)=>changeData(e)} placeholder="Tu nombre" required/>
                </div>
                <div className="input-group">
                    <label htmlFor="apellido">Apellido:</label>
                    <input type="text" id="apellidos" name="apellidos" 
                    onChange={(e)=>changeData(e)} placeholder="Tu apellido" required/>
                </div>
                <div className="input-group">
                    <label htmlFor="email">Correo Electrónico:</label>
                    <input type="email" id="email" name="correo" 
                    onChange={(e)=>changeData(e)} placeholder="tu@ejemplo.com" required/>
                </div>
                <div className="input-group">
                    <label htmlFor="password">Contraseña:</label>
                    <input type="password" id="password" 
                    onChange={(e)=>changeData(e)} name="contrasena" placeholder="********" required/>
                </div>
                <div className="input-group">
                    <label htmlFor="confirm_password">Confirmar Contraseña:</label>
                    <input type="password" id="confirm_password" 
                    onChange={(e)=>changeData(e)} name="confirm_contrasena" placeholder="********" required/>
                </div>
                <div className="input-group">
                    <label htmlFor="user_type">Tipo de Usuario:</label>
                    <select id="user_type" name="tipo" onChange={(e)=>changeData(e)} value={signUpData.tipo} required>
                        <option value="" disabled >Selecciona un tipo</option>
                        <option value="1">Alumno</option>
                        <option value="2">Maestro</option>
                    </select>
                </div>
                { signUpData.tipo == 1 ? (
                    <div className="input-group" id="curp_group" style={{display: "block"}}>
                        <label htmlFor="curp">CURP:</label>
                        <input type="text" id="curp" name="curp" onChange={(e)=>changeData(e)} placeholder="Tu CURP"/>
                    </div>
                ) : null}

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