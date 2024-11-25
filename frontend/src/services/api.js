// Add your API service code here
const API_URL = process.env.REACT_APP_API_URL;

export const fetchData = async (endpoint) => {
    const response = await fetch(`${API_URL}/${endpoint}`);
    const data = await response.json();
    return data;
};
