%% Circular Scan

A_p = 1;
F_theta_i = 1;
T_c = 5;
C_i = 1;

t = 0:0.1:30;
A_pi = A_p * F_theta_i * C_i * abs(sin(pi * t/ T_c));

figure
plot(t, A_pi)

%% Sector Scan

A_p = 1;
F_theta_i = 1;
T_sf = 4;
T_a = 0.5;
C_i = 1;

t = 0:0.1:30;
A_pi = A_p * F_theta_i * C_i * (abs(sin(pi * t/ T_sf)) + abs(sin(pi * (t - T_a)/ T_sf)));

figure
plot(t, A_pi)

%% Conical Scan



%% Helical Scan


%% Raster Scan


%% Phased Array Scan


%% Phased Array Azimuth Scan and Circular Elevation Scan


