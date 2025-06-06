import React from "react";
import { useNavigate } from "react-router-dom";

function CourseCard ({ titulo, imgName, descripcion, id }) {
    const navigate = useNavigate();
    return (
    <div className="course-card">
        <img src={imgName} alt="Curso de Programación" onClick={()=> navigate(`/capitulos/${id}`)}/>
        <h3>{titulo}</h3>
        {/* <p>{descripcion}</p> */}
        <div className="course-meta">
            <span>★ 4.7</span>
            <span>(1200 alumnos)</span>
        </div>
            <button className="btn btn-card">Ver Curso</button>
            <button className="btn btn-card" style={{ backgroundColor: "blue"}}>Comprar Certificado</button>
    </div>
    );
}

export default CourseCard