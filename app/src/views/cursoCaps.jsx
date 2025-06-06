import React, { useEffect, useState } from "react";
import "../styles/global.css";
import { useLocation } from "react-router-dom";

function CursoCaps() {
  const location = useLocation();
  const [chapters, setChapters] = useState([]);
  const [videoUrl, setVideoUrl] = useState("");
  const [modulosAbiertos, setModulosAbiertos] = useState({});

  const getChapters = async () => {
    try {
      const response = await fetch("http://localhost:8000" + location.pathname, {
        method: "GET",
        headers: { "Content-Type": "application/json" }
      });
      const data = await response.json();
      setChapters(data || []);
      if (data.length > 0) {
        setVideoUrl(embedUrl(data[0].url));
      }
    } catch (error) {
      console.error("Error al obtener los capítulos:", error);
    }
  };

  useEffect(() => {
    getChapters();
  }, [location.pathname]);

  const toggleLessons = (id) => {
    setModulosAbiertos((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  const loadYoutubeVideo = (url) => {
    setVideoUrl(embedUrl(url));
  };

  const embedUrl = (youtubeUrl) => {
    const match = youtubeUrl.match(/(?:\/|v=|be\/|embed\/)([a-zA-Z0-9_-]{11})/);
    return match ? `https://www.youtube.com/embed/${match[1]}` : "";
  };

  return (
    <section className="course-player-page">
      <div className="course-player-container">
        <div className="video-player">
          <div className="video-header">
            <h1>Curso - Capítulo {chapters[0]?.capitulo}</h1>
          </div>
          <div className="youtube-player-wrapper">
            <iframe
              width="100%"
              height="100%"
              src={videoUrl}
              title="YouTube video player"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerPolicy="strict-origin-when-cross-origin"
              allowFullScreen
            ></iframe>
          </div>
          <div className="course-description-area">
            <h2>Descripción General</h2>
            <p>{chapters[0]?.descripcion}</p>
            <p className="course-rating">★ 4.7 (1200 alumnos)</p>
          </div>
        </div>

        <div className="chapter-list-container">
          <h2>Contenido del Curso</h2>
          <div className="modules-list">
            <div className="module-item">
              <div className="module-title" onClick={() => toggleLessons("mod1")}>
                <h3>Capítulos</h3>
                <span className="toggle-icon">{modulosAbiertos["mod1"] ? "−" : "+"}</span>
              </div>
              {modulosAbiertos["mod1"] && (
                <ul className="lesson-list">
                  {chapters.map((chapter, index) => (
                    <li className="lesson-item" key={index}>
                      <a href="#" onClick={() => loadYoutubeVideo(chapter.url)}>
                        <span className="lesson-number">{chapter.capitulo}</span> {chapter.descripcion}
                        <span className="lesson-duration">{chapter.duracion} min</span>
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default CursoCaps;
