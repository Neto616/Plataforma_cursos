import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import FormularioCompra from "./formularioCompra";

// Componente CourseCard: representa una tarjeta visual de un curso.
// Muestra la imagen, título, puntuación, número de alumnos, botones para ver el curso y comprar certificado.
// Incluye un modal (FormularioCompra) que se muestra al hacer clic en "Comprar Certificado".

function CourseCard ({ titulo, imgName, descripcion, id }) {
    const navigate = useNavigate(); // Hook para redireccionar a otra ruta dentro de la app.
    const [showModal, setShowModal] = useState(false); // Estado que controla si el modal está visible o no.

    // Abre el modal de compra
    const handleOpenModal = () => setShowModal(true);

    // Cierra el modal de compra
    const handleCloseModal = () => setShowModal(false);
    
    return (
        <>
            <div className="course-card">
                {/* Imagen del curso. Al hacer clic redirige a la página de capítulos del curso */}
                <img
                    src={imgName}
                    alt="Curso de Programación"
                    onClick={() => navigate(`/capitulos/${id}`)}
                />

                {/* Título del curso */}
                <h3>{titulo}</h3>

                {/* Información estática del curso */}
                <div className="course-meta">
                    <span>★ 4.7</span>
                    <span>(1200 alumnos)</span>
                </div>

                {/* Botón para ir a la vista de capítulos del curso */}
                <button
                    className="btn btn-card"
                    onClick={() => navigate(`/capitulos/${id}`)}
                >
                    Ver Curso
                </button>

                {/* Botón que abre el formulario modal para comprar el certificado */}
                <button
                    className="btn btn-card"
                    style={{ backgroundColor: "blue" }}
                    onClick={handleOpenModal}
                >
                    Comprar Certificado
                </button>
            </div>

            {/* Modal del formulario de compra, visible si showModal es true */}
            {showModal && (
                <FormularioCompra
                    onClose={handleCloseModal}
                    courseTitle={titulo}
                />
            )}
        </>
    );
}

export default CourseCard;
