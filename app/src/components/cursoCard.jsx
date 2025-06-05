import React from "react";

function CourseCard () {
    return (
    <div className="course-card">
        <img src="https://placehold.co/300x180/E0E0E0/333333?text=Curso+1" alt="Curso de Programación" />
        <h3>Programación Web con Python</h3>
        <p>Aprende a crear aplicaciones web robustas y escalables.</p>
        <div className="course-meta">
            <span>★ 4.7</span>
            <span>(1200 alumnos)</span>
        </div>
            <button className="btn btn-card">Ver Curso</button>
    </div>
    );
}

export default CourseCard