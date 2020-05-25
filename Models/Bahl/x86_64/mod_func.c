#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _IKM_reg(void);
extern void _SlowCa_reg(void);
extern void _cad_reg(void);
extern void _epsp_reg(void);
extern void _h_reg(void);
extern void _ipulse1_reg(void);
extern void _ipulse2_reg(void);
extern void _ipulse3_reg(void);
extern void _kca_reg(void);
extern void _kfast_reg(void);
extern void _kslow_reg(void);
extern void _nap_reg(void);
extern void _nat_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," channels/IKM.mod");
    fprintf(stderr," channels/SlowCa.mod");
    fprintf(stderr," channels/cad.mod");
    fprintf(stderr," channels/epsp.mod");
    fprintf(stderr," channels/h.mod");
    fprintf(stderr," channels/ipulse1.mod");
    fprintf(stderr," channels/ipulse2.mod");
    fprintf(stderr," channels/ipulse3.mod");
    fprintf(stderr," channels/kca.mod");
    fprintf(stderr," channels/kfast.mod");
    fprintf(stderr," channels/kslow.mod");
    fprintf(stderr," channels/nap.mod");
    fprintf(stderr," channels/nat.mod");
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
