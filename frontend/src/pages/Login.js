import { useState } from 'react';
import axios from "axios";

const API = "http://127.0.0.1:8000";

function Login({ setToken }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const res = await axios.post(`${API}/login`, {
                username,
                password
            });

            const token = res.data.access_token;

            localStorage.setItem("token", token);
            setToken(token);

        } catch (err) {
            alert("Login gagal");
        }
    };
    
    return (
        <div style={{ padding: 20 }}>
            <h2>Login</h2>
            <input placeholder="username" onChange={e => setUsername(e.target.value)} />
            <br /><br />
            <input placeholder="password" type="password" onChange={e => setPassword(e.target.value)} />
            <br /><br />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;