// Importa React y useState para manejar el estado local del formulario
import React, { useState } from "react";

// Importa Link para enlaces internos y useNavigate para redirigir después del registro
import { Link, useNavigate } from "react-router-dom";

// Importa los estilos del formulario de autenticación
import "../styles/auth.css";

function SignUp() {
    // Hook para redireccionar al usuario tras registrarse exitosamente
    const navigate = useNavigate();

    // Estado para guardar los datos del formulario de registro
    const [signUpData, setSignUpData] = useState({
        nombre: "",
        apellidos: "",
        correo: "",
        contrasena: "",
        confirmar_contrasena: "",
        tipo: "1", // 1: Alumno, 2: Maestro
        curp: ""   // Solo para alumnos
    });

    // Función que actualiza el estado cuando el usuario escribe en un input
    const changeData = async (e) => {
        const { name, value } = e.target;
        setSignUpData(prev => ({ ...prev, [name]: value }));
    };

    // Función que envía los datos del formulario al backend
    const fetchSignUp = async (e) => {
        e.preventDefault(); // Evita el comportamiento por defecto del form
        try {
            // Realiza una solicitud POST al servidor con los datos de registro
            const peticion = await fetch("http://localhost:8000/crear_usuario", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(signUpData)
            });

            const resultado = await peticion.json();
            console.log(resultado);

            // Si el backend devuelve estatus falso, muestra alerta
            if (!resultado.estatus) {
                return alert("Ya existe un usuario con esas credenciales");
            }

            alert("Se ha creado su cuenta de manera exitosa");
            return navigate("/iniciar-sesion"); // Redirige al login
        } catch (error) {
            console.error("Ha ocurrido un error: ", error);
            return alert("Favor de intentarlo de nuevo más tarde");
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-box">
                <h2>Crear una Cuenta</h2>
                <form id="registroForm" onSubmit={(e) => fetchSignUp(e)}>
                    {/* Campo para el nombre */}
                    <div className="input-group">
                        <label htmlFor="nombre">Nombre:</label>
                        <input type="text" id="nombre" name="nombre"
                            onChange={changeData} placeholder="Tu nombre" required />
                    </div>

                    {/* Campo para los apellidos */}
                    <div className="input-group">
                        <label htmlFor="apellido">Apellido:</label>
                        <input type="text" id="apellidos" name="apellidos"
                            onChange={changeData} placeholder="Tu apellido" required />
                    </div>

                    {/* Campo para correo electrónico */}
                    <div className="input-group">
                        <label htmlFor="email">Correo Electrónico:</label>
                        <input type="email" id="email" name="correo"
                            onChange={changeData} placeholder="tu@ejemplo.com" required />
                    </div>

                    {/* Campo para la contraseña */}
                    <div className="input-group">
                        <label htmlFor="password">Contraseña:</label>
                        <input type="password" id="password"
                            onChange={changeData} name="contrasena" placeholder="********" required />
                    </div>

                    {/* Campo para confirmar la contraseña */}
                    <div className="input-group">
                        <label htmlFor="confirm_password">Confirmar Contraseña:</label>
                        <input type="password" id="confirm_password"
                            onChange={changeData} name="confirmar_contrasena" placeholder="********" required />
                    </div>

                    {/* Selector de tipo de usuario */}
                    <div className="input-group">
                        <label htmlFor="user_type">Tipo de Usuario:</label>
                        <select id="user_type" name="tipo"
                            onChange={changeData} value={signUpData.tipo} required>
                            <option value="" disabled>Selecciona un tipo</option>
                            <option value="1">Alumno</option>
                            <option value="2">Maestro</option>
                        </select>
                    </div>

                    {/* Si el usuario selecciona "Alumno", se muestra el campo CURP*/}
                    {signUpData.tipo == 1 ? (
                        <div className="input-group" id="curp_group" style={{ display: "block" }}>
                            <label htmlFor="curp">CURP:</label>
                            <input type="text" id="curp" name="curp"
                                onChange={changeData} placeholder="Tu CURP" />
                        </div>
                    ) : null}

                    {/* Botón de envío del formulario */}
                    <button type="submit" className="btn">Registrarse</button>

                    {/* Enlace para redirigir a iniciar sesión */}
                    <div className="links">
                        <p>¿Ya tienes cuenta?
                            <Link to="/iniciar-sesion"> Inicia sesión aquí</Link>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default SignUp;
