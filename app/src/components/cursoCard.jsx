import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import FormularioCompra from "./formularioCompra";

function CourseCard ({ titulo, imgName, descripcion, id }) {
    const navigate = useNavigate();
    const [showModal, setShowModal] = useState(false);

    const handleOpenModal = () => setShowModal(true);
    const handleCloseModal = () => setShowModal(false);
    
    return (
        <>
            <div className="course-card">
                <img src={imgName} alt="Curso de Programación" onClick={() => navigate(`/capitulos/${id}`)} />
                <h3>{titulo}</h3>
                <div className="course-meta">
                    <span>★ 4.7</span>
                    <span>(1200 alumnos)</span>
                </div>
                <button className="btn btn-card" onClick={() => navigate(`/capitulos/${id}`)}>Ver Curso</button>
                <button
                    className="btn btn-card"
                    style={{ backgroundColor: "blue" }}
                    onClick={handleOpenModal}
                >
                    Comprar Certificado
                </button>
            </div>

            {showModal && (
                <FormularioCompra onClose={handleCloseModal} courseTitle={titulo} />
            )}
        </>
    );
}

export default CourseCard