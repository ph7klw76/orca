import os

def save_input_files(filenames, directory):
    """
    Generate and save input files for each filename in the list.

    Args:
    filenames (list of str): List of filenames without extension.
    directory (str): Directory to save the files.
    """
    for filename in filenames:
        content = f"""!B3LYP DEF2-SVP OPT # Opt singlet excited Geo
%TDDFT  NROOTS  1
        IROOTMULT SINGLET
END         
%maxcore 3000
%pal nprocs 16 end
* XYZFILE 0 1 {filename}.xyz
$new_job
!B3LYP DEF2-SVP OPT # Opt triplet excited Geo
%TDDFT  NROOTS  1
        IROOTMULT TRIPLET
END         
%maxcore 3000
%pal nprocs 16 end
* XYZFILE 0 1 {filename}.xyz
$new_job
!B3LYP DEF2-SVP    # Cal Singlet excited Energy based on Opt triplet Geo
%TDDFT  NROOTS  1
        IROOTMULT SINGLET
END         
%maxcore 3000
%pal nprocs 16 end
* XYZFILE 0 1 {filename}.xyz

"""

        # Save the file
        with open(os.path.join(directory, f"{filename}.inp"), 'w') as file:
            file.write(content)

directory = "D:/labkicosmos/completed/"
# Example usage
filenames = ['10-3-O', '100-BN3', '101-DPACzBN1', '102-DPACzBN2', '103-DPACzBN3', '104-CN-BCz-BN', '105-CNCz-BNCz', '109-DtCzB-CNPm', '11-3-S', '110-D-Cz-BN', '111-S-Cz-BN', '112-BN-CP1', '113-BN-CP2', '114-SF1BN', '115-SF3BN', '116-TW-BN', '118-pCz-BN', '119-mCz-BN', '12-3-Se', '120-t-DABNA-dtB', '121-mBP-DABNA-Me', '122-tCBNDADPO', '124-BN1', '125-BN2', '126-BN-ICz-1', '127-BN-ICz-2', '128-BN-TP', '129-BIC-mCz', '130-BIC-pCz', '131-BR-OBN-2CN-BN', '132-R-OBN-4CN-BN', '133-R-BN-MeIAC', '135-v-DABNA', '136--B2', '137--B3', '138--B4', '139-CzB2-M-TB', '14-fr2', '140-Cz2B2-M-TB', '141-CzB2-M_P', '142-a-3BNOH', '143-a-3BNMes', '144-ADBNA-Me-Mes', '145-ADBNA-Me-Tip', '145-M-v-DABNA', '146-4a', '147-4b', '148-5a', '148-5b', '15-fr3', '150-BBCz-DB', '151-BBCz-R', '152-R-BN', '153-R-TBN', '156-4F-v-DABNA', '157m-B-N-N1', '158m-B-N-N2', '159mDBIC', '16-fr4', '160-BN3', '161-v-DABNA-CN-Me', '162-V-DABNA-Mes', '165-B-O-dpa', '166-B-O-Cz', '167-B-O-dmAc', '168-B-O-dpAc', '169-CzBNO', '17-3-PhQAD', '170-DMAcBNO', '171-DPAcBNO', '172-NBO', '173-PXZ-BN', '174-2PTZBN', '175-BN4', '176-BN5', '177-Cz-PTz-BN', '178-2Cz-PTZ-BN', '179-PTZBN1', '18-7-PhQAD', '180-BTZBN2', '181-PTZBN3', '182-Cz-BSN', '183-DCz-BSN', '184-CzBO', '185-CzBS', '186-CzBSe', '187-helicene-BN', '189-OAB-ABP-1', '19-BBCz-DB', '190-v-DABNA-O-Me', '191-DBNO', '192-DBSN', '193-BSBS-N1', '194-m-DiNBO', '195-BOBO-Z', '196-BOBS-Z', '197-BSBS-Z', '2-DOBNA', '20-CzBN', '200-QAO', '201-3-PhQAD', '202-7-PhQA', '203-DiKTa', '204-mes3Dikta', '206-DQAO.', '207-OQA', '208-SQAO', '209-QA-PF', '21-CzBNCz', '210-QA-PCN', '211-QA-PMO', '212-QA-PCZ', '213-QAD-Czl', '214-QAD-2Cz', '215-QAD-mTDPA', '216-QAO-PhCz', '217-QAOCz1', '218-QAOCz2', '219-QAOCz3', '22-DABNA-2', '220-Cz-PhDiKTa', '221-Cz-DiKTa', '222-3Cz-DiKTa', '223-TOAT', '224-5', '225-mBDPA-TOAT', '226-pBDPA-TOAT', '227-23-CZ', '228-25-CZ', '23-DDiKTa', '230-QA--1', '231-QA-2', '232-Hel-DiDiKTa', '234-tBisICz', '235-tPBisICz', '236-DiICzMes', '237-t3IDCz', '238-p3IDCz', '24-DtByCzB', '240-AZA-BN', '241-OAB-ABP-1', '241-PXZ-BN', '243-DTCzBTPTRZ', '244-VTCzBN', '245-TCz-VTCzBN', '247-DBTN-2', '248-BN-STO', '249-BN-TP-N1', '25-DtBuPhCzB', '250-BN-TP-N2', '251-BN-TP-N3', '252-BN-TP-N4', '254-2PyBN', '255-2PyBN', '256-4PyBN', '26-fr5', '27-in-TABNA', '28-mes3Dikta', '29-OAB-ABP-1', '3-DABNA', '30-ol4', '31-ol5', '32-ol6', '33-ol7', '34-ol8', '35-QAO-Dad', '36-QAO', '37-t-DABNA', '38-TABNA', '39-TBA-TPA', '4-ADBNA', '41-B3', '42-B4', '43-DQAO', '44-OQAO', '45-cisQA-2', '46-SQAO', '47-TOAT', '48-v-DABNA', '49-DABNA-1', '5-OAB-ABP', '51-PhCz-TSOBA', '55-TPA-TSOBA', '6-1-S', '60-CzBNO', '61-DMAcBNO', '62-DPAcBNO', '64-Cz-PTZ-BN', '65-2Cz-PTZ-BN', '67-TPZZBN', '68-DPXZCZBN', '7-1-Se', '70-2b', '71-2c', '72-2d', '73-1', '74-DOBNA-OAr', '76-TBN-TPA', '77-Tcz-BN', '78-2F-BN', '79-3F-BN', '8-2-S', '80-4F-BN', '81-m-Cz-BNCz', '84-y-Cb-B', '85-TCz-B', '86-DACz-B', '87-DMAC-BN', '88-BN-DPAC', '89-DABNA-NP-TB', '9-2-Se', '90-CzDABNA-NP-M-TB', '91-Cz2DABNA-NP-M-TB', '92-CzDABNA-NP', '93-CzDABNA-NP-TB-H', '94-DABNA-NP-M', '95-PAB', '96-tDMAC-BN', '97-tDPAC-BN', '98-BN1', '99-BN2']
for f in filenames:
    input_files = save_input_files(filenames, directory)

