// Importación de React y hooks
import React, { useEffect, useState } from 'react';

// Importación de navegación y enlaces internos desde React Router
import { Link, useNavigate } from "react-router-dom";

// Importación de los estilos compartidos de autenticación
import "../styles/auth.css";

function Login() {
    // Hook de navegación para redirigir después del inicio de sesión exitoso
    const navigate = useNavigate();

    // Estado local para guardar los datos ingresados en el formulario
    const [loginData, setLoginData] = useState({
        correo: "",
        contrasena: ""
    });

    // Maneja los cambios en los inputs del formulario y actualiza el estado
    const changeData = async (e) => {
        const { name, value } = e.target;
        setLoginData(prev => ({ ...prev, [name]: value }));
    };

    // Función que se encarga de enviar los datos al backend para verificar el login
    const fetchLogin = async (e) => {
        try {
            e.preventDefault(); // Previene el comportamiento por defecto del formulario

            // Se hace una petición POST al backend con los datos del login
            const peticion = await fetch("http://localhost:8000/iniciar-sesion", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(loginData)
            });

            const respuesta = await peticion.json(); // Se parsea la respuesta
            console.log(respuesta); // Se muestra en consola para depuración

            // Si el estatus es falso, se muestra alerta de error
            if (!respuesta.estatus) return alert("Credenciales incorrectas");

            // Si todo está bien, se muestra mensaje de bienvenida y se redirige al inicio
            alert(respuesta.result.message);
            navigate(`/`);
            return;
        } catch (error) {
            // Captura errores de red o servidor
            console.error("Ha sucedido un error: ", error);
            alert("Favor de intentarlo de nuevo más tarde");
        }
    };

    // JSX del formulario de login
    return (
        <div className="auth-container">
            <div className="auth-box">
                <h2>Iniciar Sesión</h2>
                <form onSubmit={(e) => fetchLogin(e)}>
                    {/* Campo para el correo electrónico */}
                    <div className="input-group">
                        <label htmlFor="email">Correo Electrónico:</label>
                        <input
                            type="email"
                            id="email"
                            name="correo"
                            placeholder="tu@ejemplo.com"
                            onChange={changeData}
                            required
                        />
                    </div>

                    {/* Campo para la contraseña */}
                    <div className="input-group">
                        <label htmlFor="password">Contraseña:</label>
                        <input
                            type="password"
                            id="password"
                            name="contrasena"
                            placeholder="********"
                            onChange={changeData}
                            required
                        />
                    </div>

                    {/* Botón para enviar el formulario */}
                    <button type="submit" className="btn">Entrar</button>

                    {/* Enlace a la vista de registro */}
                    <div className="links">
                        <p>¿No tienes cuenta? <Link to="/sign-up">Regístrate aquí</Link></p>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;
