import { useEffect, useState } from "react";
import axios from "axios";

const API = "http://127.0.0.1:8000";

function Dashboard() {
  const [data, setData] = useState([]);
  const [result, setResult] = useState("");
  const [visibleCount, setVisibleCount] = useState(10);

  const [jumlah, setJumlah] = useState("");
  const [harga, setHarga] = useState("");
  const [diskon, setDiskon] = useState("");

  const token = localStorage.getItem("token");

  useEffect(() => {
    axios.get(`${API}/sales`)
      .then(res => setData(res.data))
      .catch(() => alert("Gagal ambil data"));
  }, []);

  const handlePredict = async () => {
    try {
        console.log("TOKEN:", token);
        console.log("INPUT:", jumlah, harga, diskon);

        const res = await axios.post(`${API}/predict`, {
        jumlah_penjualan: Number(jumlah),
        harga: Number(harga),
        diskon: Number(diskon)
        }, {
        headers: {
            Authorization: `Bearer ${token}`
        }
        });

        setResult(res.data.prediction);

    } catch (err) {
        console.log("ERROR DETAIL:", err.response?.data || err.message);
        alert("Gagal predict");
    }
};

  return (
    <div style={{ padding: 20, background: "#f5f5f5", minHeight: "100vh" }}>
        
        <h1 style={{ marginBottom: 20 }}>AI Sales Prediction System</h1>

        <div style={{
        background: "#fff",
        padding: 15,
        marginBottom: 20,
        borderRadius: 8,
        boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
        }}>
        <h3>Data Penjualan</h3>

        <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead style={{ background: "#eee" }}>
            <tr>
                <th>Produk</th>
                <th>Jumlah</th>
                <th>Harga</th>
                <th>Diskon</th>
                <th>Status</th>
            </tr>
            </thead>

            <tbody>
            {data.slice(0, visibleCount).map((item, i) => (
                <tr key={i} style={{ textAlign: "center", borderTop: "1px solid #ddd" }}>
                <td>{item.product_name}</td>
                <td>{item.jumlah_penjualan}</td>
                <td>{item.harga}</td>
                <td>{item.diskon}%</td>

                <td>
                    <span style={{
                    padding: "4px 8px",
                    borderRadius: 5,
                    color: item.status === "Laris" ? "green" : "red",
                    fontWeight: "bold"
                    }}>
                    {item.status}
                    </span>
                </td>

                </tr>
            ))}
            </tbody>
        </table>
        {visibleCount < data.length && (
            <button
                style={{
                marginTop: 10,
                padding: "8px 16px",
                background: "#007bff",
                color: "white",
                border: "none",
                borderRadius: 5
                }}
                onClick={() => setVisibleCount(visibleCount + 10)}
            >
                Load More
            </button>
            )}
        </div>

        <div style={{
        background: "#fff",
        padding: 15,
        borderRadius: 8,
        boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
        }}>
        <h3>Prediksi Produk</h3>

        <div style={{ marginBottom: 10 }}>
            <input placeholder="Jumlah Penjualan" onChange={e => setJumlah(e.target.value)} />
        </div>

        <div style={{ marginBottom: 10 }}>
            <input placeholder="Harga" onChange={e => setHarga(e.target.value)} />
        </div>

        <div style={{ marginBottom: 10 }}>
            <input placeholder="Diskon (%)" onChange={e => setDiskon(e.target.value)} />
        </div>

        <button
            style={{
            padding: "8px 16px",
            background: "#007bff",
            color: "white",
            border: "none",
            borderRadius: 5
            }}
            onClick={handlePredict}
        >
            Predict
        </button>

        {result && (
            <h4 style={{ marginTop: 15 }}>
            Hasil: <b>{result}</b>
            </h4>
        )}
        </div>

    </div>
    );
}

export default Dashboard;