import { useState, useEffect } from 'react';
import axios from 'axios';

// Assume API is at root /api/auth since we proxy /api to App0
// Our custom implementation: /api/auth/login
const API_URL = '/api/auth';

function App() {
  const [token, setToken] = useState(localStorage.getItem('access_token'));
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (token) {
      // Decode token or fetch user profile if endpoint exists.
      // For now, just assume logged in.
      // We could verify token validity here.
    }
  }, [token]);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axios.post(`${API_URL}/login`, {
        username,
        password
      });
      const { access, refresh } = response.data;
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      setToken(access);
    } catch (err) {
        console.error(err);
      setError('Login failed. Please check your credentials.');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setToken(null);
  };

  if (!token) {
    return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="card shadow">
              <div className="card-header bg-primary text-white">
                <h3 className="mb-0">Login</h3>
              </div>
              <div className="card-body">
                {error && <div className="alert alert-danger">{error}</div>}
                <form onSubmit={handleLogin}>
                  <div className="mb-3">
                    <label className="form-label">Username</label>
                    <input
                      type="text"
                      className="form-control"
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Password</label>
                    <input
                      type="password"
                      className="form-control"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                    />
                  </div>
                  <button type="submit" className="btn btn-primary w-100">Login</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="card shadow">
        <div className="card-body text-center">
          <h1 className="display-4">Hello World!</h1>
          <p className="lead">You are successfully authenticated.</p>
          <div className="alert alert-success">
            Token: {token.substring(0, 20)}...
          </div>
          <button onClick={handleLogout} className="btn btn-danger">Logout</button>
        </div>
      </div>
    </div>
  );
}

export default App;
