import numpy as np
def haversine_great_circle_distance(theta1,phi1,theta2,phi2):
    """Computes great circle distance between any number of paired
    locations using the haversine formula, which is known to be accurate
    for short distances. All angles in radians.
    Greek letter convention is theta for colatitude, phi for azimuth/longitude
    """
    lambda1 = np.pi/2-theta1
    lambda2 = np.pi/2-theta2
    delta_lambda = lambda2-lambda1
    delta_phi = phi2-phi1
    def hav(x):
        """Haversine function"""
        return np.sin(x*.5)**2.
    def archav(theta):
        """Inverse haversine"""
        return 2.*np.arcsin(np.sqrt(theta))
    def archav2(theta):
        """Inverse haversine using arctan2"""
        return 2.*np.arctan2(np.sqrt(theta),np.sqrt(1.-theta))

    hav_dist = hav(delta_lambda)+np.cos(lambda1)*np.cos(lambda2)*hav(delta_phi)
    
    dist = archav2(hav_dist)
    return dist

if __name__ == '__main__':
    lat1,lon1 = 70.,10.
    lat2,lon2 = 80.,10.

    theta1,phi1 = np.radians(90-lat1),np.radians(lon1)
    theta2,phi2 = np.radians(90-lat2),np.radians(lon2)

    dist = haversine_great_circle_distance(theta1,phi1,theta2,phi2)

    print('Distance between \n{},{} and {},{}\n is {}'.format(lat1,lon1,
                                                                lat2,lon2,
                                                                np.degrees(dist)))    
