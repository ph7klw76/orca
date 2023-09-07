# orca
to calculate spin-orbit coupling use:
! wB97X-D3 DEF2-SVP

%TDDFT  NROOTS  10

        DOSOC   TRUE
end
%maxcore 3000
%pal
nprocs 16
end
* xyzfile 0 1 molecule_16.xyz
