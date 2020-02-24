#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _IKM_reg();
extern void _SlowCa_reg();
extern void _cad_reg();
extern void _epsp_reg();
extern void _h_reg();
extern void _ipulse1_reg();
extern void _ipulse2_reg();
extern void _ipulse3_reg();
extern void _kca_reg();
extern void _kfast_reg();
extern void _kslow_reg();
extern void _nap_reg();
extern void _nat_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," IKM.mod");
fprintf(stderr," SlowCa.mod");
fprintf(stderr," cad.mod");
fprintf(stderr," epsp.mod");
fprintf(stderr," h.mod");
fprintf(stderr," ipulse1.mod");
fprintf(stderr," ipulse2.mod");
fprintf(stderr," ipulse3.mod");
fprintf(stderr," kca.mod");
fprintf(stderr," kfast.mod");
fprintf(stderr," kslow.mod");
fprintf(stderr," nap.mod");
fprintf(stderr," nat.mod");
fprintf(stderr, "\n");
    }
_IKM_reg();
_SlowCa_reg();
_cad_reg();
_epsp_reg();
_h_reg();
_ipulse1_reg();
_ipulse2_reg();
_ipulse3_reg();
_kca_reg();
_kfast_reg();
_kslow_reg();
_nap_reg();
_nat_reg();
}
