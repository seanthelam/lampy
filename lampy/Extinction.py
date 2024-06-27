class Extinction:
    def __init__(self, dustmap, lbd):
        """
        Initialize the Extinction class with the given dustmap and coordinates

        Parameters
        ----------
        dustmap : string
            The name of the dustmap to use ('edenhofer', 'marshall', 'bayestar').
        lbd : SkyCoord
            Sky coordinates for the extinction query.
        """
        
        self.dustmap = dustmap
        self.lbd = lbd
        self.extinction_data_ha, self.extinction_data_hb = self._get_extinction_parameters()

    def _get_extinction_parameters(self):
        """
        Get the extinction parameters for the specified dustmap.

        Returns
        -------
        extinction_data_ha, extinction_data_hb : array
            Extinction data for H-alpha and H-beta.
        """

        if self.dustmap == 'edenhofer':
            wave_ha = np.array([6562.8]) * u.AA
            A_V_to_A_ha = extinction_law(wave_ha.to(u.AA).value, 1.)
            wave_hb = np.array([4861.32]) * u.AA
            A_V_to_A_hb = extinction_law(wave_hb.to(u.AA).value, 1.)
            
            eden_mean = eden(self.lbd, mode='mean')
            extinction_data_ha = A_V_to_A_ha * (eden_mean * 2.8) # Convert E(B-V) to AV
            extinction_data_hb = A_V_to_A_hb * (eden_mean * 2.8)

        elif self.dustmap == 'marshall':
            wave_Ks = 2.17 * u.micron
            A_KS_to_A_v = 1. / extinction_law(np.array([wave_Ks.to(u.AA).value]), 1.)
            wave_ha = np.array([6562.8]) * u.AA
            A_V_to_A_ha = extinction_law(wave_ha.to(u.AA).value, 1.)
            wave_hb = np.array([4861.32]) * u.AA
            A_V_to_A_hb = extinction_law(wave_hb.to(u.AA).value, 1.)
            
            extinction_data_ha = 10 ** (-0.4 * A_KS_to_A_v * A_V_to_A_ha * marsh(self.lbd))
            extinction_data_hb = 10 ** (-0.4 * A_KS_to_A_v * A_V_to_A_hb * marsh(self.lbd))

        elif self.dustmap == 'bayestar':
            wave_ha = np.array([6562.8]) * u.AA
            A_V_to_A_ha = extinction_law(wave_ha.to(u.AA).value, 1.)
            wave_hb = np.array([4861.32]) * u.AA
            A_V_to_A_hb = extinction_law(wave_hb.to(u.AA).value, 1.)
            
            extinction_data_ha = A_V_to_A_ha * (bay(self.lbd) * 2.742) # Convert E(B-V) to AV
            extinction_data_hb = A_V_to_A_hb * (bay(self.lbd) * 2.742)

        else:
            raise ValueError(f"Unknown dustmap: {dustmap}")

        return extinction_data_ha, extinction_data_hb
        
