import axios from "axios";

const FEAGI_URL = "http://localhost:8000/v1";

const FeagiAPI = {
  async getBaselineSensory() {
    const response = await axios.get(
      `${FEAGI_URL}/feagi/feagi/gui_baseline/ipu`,
      {
        headers: {},
        params: {},
      }
    );
    return response.data;
  },

  async getBaselineMotor() {
    const response = await axios.get(
      `${FEAGI_URL}/feagi/feagi/gui_baseline/opu`,
      {
        headers: {},
        params: {},
      }
    );
    return response.data;
  },

  async getBaselineMorphology() {
    const response = await axios.get(
      `${FEAGI_URL}/feagi/feagi/gui_baseline/morphology`,
      {
        headers: {},
        params: {},
      }
    );
    return response.data;
  },
};

export default FeagiAPI;
