from odoo import api, fields, models, _


class OeHealthPatientEvaluationExtension(models.Model):
    _inherit = 'oeh.medical.evaluation'
    _description = "Patient Evaluation Extension"

    EVALUATION_TYPE = [
            ('New Complaint', 'New Complaint'),
            ('Follow Up', 'Follow Up'),
            ('Check Up', 'Check Up'),
            ('Phone Call', 'Phone Call'),
            ('Telemedicine', 'Telemedicine'),
    ]

    EVALUATION_STATE = [        
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    @api.multi
    def set_to_completed(self):
        return self.write({'state': 'Completed'})

    state = fields.Selection(EVALUATION_STATE, string='State', readonly=True, default=lambda *a: 'In Progress')
    evaluation_type = fields.Selection(EVALUATION_TYPE, string='Evaluation Type', required=True, index=True, default=lambda *a: 'New Complaint')

    # extended fields
    chief_complaint = fields.Text(string='Chief Complaint', help='Chief Complaint')
    indication = fields.Many2many('oeh.medical.pathology', string="Indication")
    height = fields.Float(string='Height (cm)', required=True)

    # added signs and symptoms fields
    # general
    general_symptom_fever = fields.Selection( [('Intermittent', 'Intermittent'), ('continuous', 'continuous'),
    ('step-ladder','step-ladder'),('high grade','High grade'),('low grade','Low Grade')],'Fever')
    general_symptom_malaise = fields.Boolean(string="Malaise")
    general_symptom_joint_ache = fields.Boolean(string="Joint Aches")
    general_symptom_dizziness = fields.Boolean(string="Dizziness")
    general_symptom_chills = fields.Boolean(string="Chills")
    general_symptom_night_sweats = fields.Boolean(string="Night Sweats")
    general_symptom_weight = fields.Selection([('gain', 'Gain'), ('loss', 'Loss')],'Weight')
    general_symptom_easy_fatigability = fields.Boolean(string="Easy Fatigability")
    general_symptom_pain_site = fields.Char(string="Site")
    general_symptom_pain_onset = fields.Date(string="Onset")
    general_symptom_pain_character = fields.Char(string="Character")
    general_symptom_pain_severity = fields.Char(string="Severity")
    general_symptom_pain_radiation = fields.Char(string="Radiation")
    general_symptom_pain_aggravating = fields.Char(string="Aggravating factors")
    general_symptom_pain_relieving = fields.Char(string="Relieving factors")
    general_symptom_pain_associated = fields.Char(string="Associated symptoms")
    general_symptom_pain_possible_etiology = fields.Char(string="Possible etiology")

    general_symptom_swelling_site = fields.Char(string="Site")
    general_symptom_swelling_progression = fields.Selection([('slow', 'Slow'), ('rapid', 'Rapid')],'Progression')
    general_symptom_swelling_associated_pain = fields.Boolean(string="Associated pain")
    general_symptom_swelling_itchy = fields.Boolean(string="Itchy")
    general_symptom_swelling_associated_symptom = fields.Char(string="Associated symptoms")
    general_symptom_swelling_possible_etiology = fields.Char(string="Possible etiology")
    general_symptom_swelling_others = fields.Char(string="Possible etiology")
    general_symptom_swelling_left_breast_lump = fields.Boolean(string="Left Breast Lump")
    general_symptom_swelling_right_breast_lump = fields.Boolean(string="Right Breast Lump")
    general_symptom_swelling_rash = fields.Boolean(string="Rash")
    general_symptom_swelling_rash_others = fields.Boolean(string="Others")

    general_sign_unwell = fields.Boolean(string="Unwell")
    general_sign_acutely_ill = fields.Boolean(string="Acutely ill-looking")
    general_sign_chronically_ill = fields.Boolean(string="Chronically ill-looking")
    general_sign_wasted = fields.Boolean(string="Wasted")
    general_sign_stunted = fields.Boolean(string="Stunted")
    general_sign_fluffy_hair = fields.Boolean(string="Fluffy hair")
    general_sign_pallor = fields.Boolean(string="Pallor")
    general_sign_jaundice = fields.Boolean(string="Jaundice")
    general_sign_central_cyanosis = fields.Boolean(string="Central cyanosis")
    general_sign_dehydration = fields.Selection([('mild', 'Mild'), ('moderate', 'Moderate'),
    ('severe','Severe')],'Dehydration')
    general_sign_digital_clubbing = fields.Boolean(string="Digital clubbing")
    general_sign_peripheral_cyanosis = fields.Boolean(string="Peripheral cyanosis")
    general_sign_simian_crease = fields.Boolean(string="Simian crease")
    general_sign_peripheral_lymph_site = fields.Char(string="Site")
    general_sign_peripheral_lymph_character = fields.Char(string="Character")
    general_sign_peripheral_lymph_changes = fields.Char(string="Overlying skin changes")
    general_sign_pedal_edema = fields.Selection([('pitting', 'Pitting'), ('non pitting', 'Non Pitting'),
    ],'Pedal edema')
    general_sign_rashes_location = fields.Char(string="Location")
    general_sign_rashes_nature = fields.Char(string="Nature")
    general_sign_swelling_site = fields.Char(string="Site")
    general_sign_swelling_size = fields.Char(string="Size")
    general_sign_swelling_consistency = fields.Char(string="Consistency")
    general_sign_swelling_overlying_skin = fields.Char(string="Overlying skin changes")
    general_sign_swelling_attached_to_skin = fields.Boolean(string="Attached to skin")
    general_sign_swelling_attached_to_underlying = fields.Boolean(string="Attached to underlying structures")
    general_sign_differential_warmth = fields.Boolean(string="Differential warmth")
    general_sign_swelling_mobile = fields.Selection([('free', 'Free'), ('partial', 'Partial'),('not mobile','Not Mobile')
    ],'Pedal edema')
    general_sign_swelling_fluctuant = fields.Boolean(string="Fluctuant")
    general_sign_swelling_pulsatile = fields.Boolean(string="Pulsatile")
    general_sign_additional_findings = fields.Text(string="Additional findings")
    
    # Central Nervous System
    # symptom
    cns_symptom_headache_nature = fields.Char(string="Nature")
    cns_symptom_headache_side = fields.Char(string="Side")
    cns_symptom_headache_radiation = fields.Char(string="Radiation")
    cns_symptom_headache_severity = fields.Char(string="Severity")
    cns_symptom_headache_associated_symptoms = fields.Char(string="Associated symptoms")
    cns_symptom_headache_aggravating_factors = fields.Char(string="Aggravating factors")
    cns_symptom_headache_relieving_factors = fields.Char(string="Relieving factors")
    cns_symptom_headache_aura = fields.Char(string="Aura")

    cns_symptom_limb_weakness = fields.Boolean(string="Limb weakness")
    cns_symptom_limb_blurry_vision = fields.Boolean(string="Blurry vision")
    cns_symptom_limb_insomnia = fields.Boolean(string="Insomnia")
    cns_symptom_limb_convulsion = fields.Char(string="Convulsion")
    cns_symptom_limb_amnesia = fields.Boolean(string="Amnesia")
    cns_symptom_limb_sphincteric_disturbance = fields.Selection([('hypoactive', 'Hypoactive'), ('Hyperactive', 'Partial')
    ],'Sphincteric disturbance')
    cns_symptom_limb_others = fields.Text(string="Others")

    # signs
    cns_sign_conscious = fields.Boolean("Conscious")
    cns_sign_unconscious = fields.Boolean("Unconscious")
    cns_sign_orientation_oriented = fields.Selection([('time', 'Time'),('place', 'Place'),('person','Person')
    ],'Orientation')
    cns_sign_orientation_not_oriented = fields.Boolean("Not oriented")
    cns_glasgow_coma_score_eye_opening_score = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4')],'Eye opening score')
    cns_glasgow_coma_score_motor_score = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],'Best motor response score')
    cns_glasgow_coma_score_verbal_score = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')],'Best verbal response score')
    
    cns_sign_cranial_nerve_deficits = fields.Boolean(string="Cranial nerve deficits")
    cns_sign_fasciculations = fields.Boolean(string="Fasciculations")
    cns_sign_right_upper_limb = fields.Selection([('normal', 'normal'),('weakness', 'weakness'),('hypertonia','hypertonia'),
    ('hypotonia','hypotonia'),('hyperreflexia','hyperreflexia'),('hyporeflexia','hyporeflexia')],'Right upper limb')
    cns_sign_right_lower_limb = fields.Selection([('normal', 'normal'),('weakness', 'weakness'),('hypertonia','hypertonia'),
    ('hypotonia','hypotonia'),('hyperreflexia','hyperreflexia'),('hyporeflexia','hyporeflexia')],'Right lower limb')
    cns_sign_left_upper_limb = fields.Selection([('normal', 'normal'),('weakness', 'weakness'),('hypertonia','hypertonia'),
    ('hypotonia','hypotonia'),('hyperreflexia','hyperreflexia'),('hyporeflexia','hyporeflexia')],'Left upper limb')
    cns_sign_left_lower_limb = fields.Selection([('normal', 'normal'),('weakness', 'weakness'),('hypertonia','hypertonia'),
    ('hypotonia','hypotonia'),('hyperreflexia','hyperreflexia'),('hyporeflexia','hyporeflexia')],'Left lower limb')
    cns_sign_babinski_reflex = fields.Boolean(string="Babinski reflex")
    cns_sign_ankle_clonus = fields.Boolean(string="Ankle clonus")
    cns_sign_loss_of_sensation = fields.Selection([('fine touch','fine touch'),('crude touch','crude touch'),('pain','pain'),
    ('joint position','joint position'),('vibration sense','vibration sense')],'Loss of sensation')
    cns_sign_gait = fields.Selection([('normal','normal'),('antalgic','antalgic'),('swaddling','swaddling'),
    ('hemiplegic','hemiplegic'),('diplegic','diplegic'),('choreiform','choreiform'),
    ('ataxia','ataxia'),('Parkinsonian','Parkinsonian')],'Loss of sensation')
    cns_sign_dysdiadochokinesis = fields.Boolean(string="Dysdiadochokinesis")
    cns_sign_intention_tremor = fields.Boolean(string="Intention tremor")
    cns_sign_rebound_phenomena = fields.Boolean(string="Rebound phenomena")
    cns_sign_dysmetria = fields.Boolean(string="Dysmetria")
    cns_sign_nystagmus = fields.Boolean(string="Nystagmus")
    cns_sign_dysarthria = fields.Boolean(string="Dysarthria")
    cns_sign_titubation = fields.Boolean(string="Titubation")
    cns_sign_torticollis = fields.Boolean(string="Torticollis")
    cns_sign_romberg_sign = fields.Selection([('positive','positive'),('negative','negative')],'Romberg sign')
    cns_sign_others = fields.Text(string="Others")

    # Musculoskeletal system
    # symptoms
    symptom_muscle_low_back_pains = fields.Boolean(string="Low back pains")
    symptom_muscle_muscle_aches = fields.Boolean(string="Muscle aches")
    symptom_muscle_bone_pains = fields.Boolean(string="Bone pains")
    symptom_muscle_fractures = fields.Boolean(string="Fractures")
    symptom_muscle_dislocations = fields.Boolean(string="Dislocations")
    symptom_muscle_others = fields.Text(string="Others")  

    # signs
    sign_muscle_fractures = fields.Boolean(string="Fractures")
    sign_muscle_dislocation = fields.Boolean(string="Dislocation")
    sign_muscle_scoliosis = fields.Boolean(string="Scoliosis")
    sign_muscle_lordosis = fields.Boolean(string="Lordosis")
    sign_muscle_kyphosis = fields.Boolean(string="Kyphosis")
    sign_muscle_genu_valga = fields.Boolean(string="Genu valga")
    sign_muscle_genu_vara = fields.Boolean(string="Genu vara")
    sign_muscle_windswept_deformity = fields.Boolean(string="Windswept deformity")
    sign_muscle_clubfoot = fields.Boolean(string="Clubfoot")
    sign_muscle_amputations = fields.Boolean(string="Amputations")
    sign_muscle_others = fields.Text(string="Others")

    # Respiratory system
    # symptoms
    symptom_respiratory_coryza = fields.Boolean(string="Coryza")
    symptom_respiratory_cough = fields.Boolean(string="Cough")
    symptom_respiratory_sore_throat = fields.Boolean(string="Sore throat")
    symptom_respiratory_difficulty_with_breathing = fields.Boolean(string="Difficulty with breathing")
    symptom_respiratory_breathlessness = fields.Boolean(string="Breathlessness")
    symptom_respiratory_fast_breathing = fields.Boolean(string="Fast breathing")
    symptom_respiratory_mouth_breathing = fields.Boolean(string="Mouth breathing")
    symptom_respiratory_noisy_breathing = fields.Boolean(string="Noisy breathing")
    symptom_respiratory_night_sweats = fields.Boolean(string="Night sweats")
    symptom_respiratory_orthopnea = fields.Boolean(string="Orthopnea")
    symptom_respiratory_paroxysmal_nocturnal_dypsnea = fields.Boolean(string="Paroxysmal nocturnal dypsnea")
    symptom_respiratory_haemoptysis = fields.Boolean(string="Haemoptysis")
    symptom_respiratory_hoarseness = fields.Boolean(string="Hoarseness")
    symptom_respiratory_stridor = fields.Boolean(string="Stridor")
    symptom_respiratory_snoring = fields.Boolean(string="Snoring")
    symptom_respiratory_nasal_stuffiness = fields.Boolean(string="Nasal stuffiness")
    symptom_respiratory_others = fields.Text(string="Others")  

    # signs
    sign_respiratory_respiratory_distress = fields.Boolean(string="Respiratory distress")
    sign_respiratory_nasal_stuffiness = fields.Boolean(string="Nasal stuffiness")
    sign_respiratory_pursed_lip = fields.Boolean(string="Pursed lip")
    sign_respiratory_hepatic_fetor = fields.Boolean(string="Hepatic fetor")
    sign_respiratory_barrel_chest = fields.Boolean(string="Barrel chest")
    sign_respiratory_pigeon_chest = fields.Boolean(string="Pigeon chest (pectum carinatum)")
    sign_respiratory_funnel_chest = fields.Boolean(string="Funnel chest (pectum excavatum)")
    sign_respiratory_scarification_marks = fields.Boolean(string="Scarification marks")
    sign_respiratory_rickety_rosary = fields.Boolean(string="Rickety rosary")
    sign_respiratory_uniform_chest_expansion = fields.Boolean(string="Uniform chest expansion")

    sign_respiratory_tracheal_deviation = fields.Selection([('normal','Normal'),('left','Left'),
    ('right','Right')],'Tracheal deviation')
    sign_respiratory_reduced_expansion = fields.Selection([('left','Left'),('right','Right')
    ],'Reduced expansion')
    sign_respiratory_resonant_percussion_note = fields.Selection([('left','Left'),('right','Right')
    ],'Resonant percussion note')
    sign_respiratory_hyperresonant_percussion_note = fields.Selection([('left','Left'),('right','Right')
    ],'Hyperresonant percussion note')
    sign_respiratory_dull_percussion_note = fields.Selection([('left','Left'),('right','Right')
    ],'Dull percussion note')
    sign_respiratory_stony_dull_percussion_note = fields.Selection([('left','Left'),('right','Right')
    ],'Stony dull percussion note')
    sign_respiratory_vesicular_breath_sounds = fields.Selection([('left','Left'),('right','Right')
    ],'Vesicular breath sounds')
    sign_respiratory_crepitations = fields.Selection([('left','Left'),('right','Right')
    ],'Crepitations')
    sign_respiratory_fine_crackles = fields.Selection([('left','Left'),('right','Right')
    ],'Fine crackles')
    sign_respiratory_coarse_crackles = fields.Selection([('left','Left'),('right','Right')
    ],'Coarse crackles')
    sign_respiratory_others = fields.Text(string="Others")

    # Cardiovascular system
    # symptom
    symptom_cardio_chest_pain_site = fields.Char(string="Site")
    symptom_cardio_chest_pain_onset = fields.Char(string="Onset")
    symptom_cardio_chest_pain_severity = fields.Char(string="Severity")
    symptom_cardio_chest_pain_nature = fields.Char(string="Nature")
    symptom_cardio_chest_pain_radiation = fields.Char(string="Radiation")
    symptom_cardio_chest_pain_duration = fields.Char(string="Duration")
    symptom_cardio_chest_pain_aggravating_factors = fields.Char(string="Aggravating factors")
    symptom_cardio_chest_pain_relieving_factors = fields.Char(string="Relieving factors")
    symptom_cardio_chest_pain_associated_symptoms = fields.Char(string="Associated symptoms")
    symptom_cardio_palpitations = fields.Boolean(string="Palpitations")
    symptom_cardio_claudication = fields.Boolean(string="Claudication")
    symptom_cardio_others = fields.Boolean(string="Others")

    # sign
    sign_cardio_cold_extremities = fields.Boolean(string="Cold extremities")
    sign_cardio_bruits = fields.Boolean(string="Bruits")
    sign_cardio_splinter_hemorrhage = fields.Boolean(string="Splinter hemorrhage")
    sign_cardio_osler_nodes = fields.Boolean(string="Osler nodes")
    sign_cardio_janeway_nodes = fields.Boolean(string="Janeway nodes")
    sign_cardio_rhythm = fields.Selection([('regular','regular'),('irregularly irregular','irregularly irregular'),
    ('regularly irregular','regularly irregular')],'Rhythm')
    sign_cardio_synchronicity = fields.Selection([('synchronous','Synchronous'),
    ('radioradial delay','radioradial delay'),('radiofemoral delay','radiofemoral delay')],'Synchronicity')
    sign_cardio_thickened_arterial_wall = fields.Boolean(string="Thickened arterial wall")
    sign_cardio_locomotor_brachialis = fields.Boolean(string="Locomotor brachialis")
    sign_cardio_jvp = fields.Selection([('normal','Normal'),('raised','Raised')],'JVP')
    sign_cardio_apex_beat = fields.Selection([('normal','Normal'),('displaced','displaced'),('tapping','tapping'),
    ('diffuse','diffuse'),('double impulse','double impulse'),('heave','heave'),
    ('thrills','thrills')],'Apex beat')
    sign_cardio_heart_sounds = fields.Selection([('first','first'),('second','second'),('third','third'),
    ('fourth','fourth')],'Heart sounds')
    sign_cardio_heart_murmurs = fields.Selection([('nil','nil'),('pansystolic','pansystolic'),('early diastolic','early diastolic'),
    ('mid-systolic','mid-systolic'),('mid-diastolic','mid-diastolic'),('continuous','continuous')],'Murmurs')
    sign_cardio_others = fields.Text(string="Others")

    # Abdomen
    symptom_abdomen_abdominal_site = fields.Char(string="Site")
    symptom_abdomen_abdominal_onset = fields.Char(string="Onset")
    symptom_abdomen_abdominal_nature = fields.Char(string="Nature")
    symptom_abdomen_abdominal_duration = fields.Char(string="Duration")
    symptom_abdomen_abdominal_relieving_factors = fields.Char(string="Relieving factors")
    symptom_abdomen_abdominal_aggravating_factors = fields.Char(string="Aggravating factors")
    symptom_abdomen_abdominal_severity = fields.Char(string="Severity")
    symptom_abdomen_abdominal_radiation = fields.Char(string="Radiation")
    symptom_abdomen_abdominal_associated_symptoms = fields.Text(string="Associated symptoms")
    symptom_abdomen_distension = fields.Boolean(string="Distension")
    symptom_abdomen_nausea = fields.Boolean(string="Nausea")
    symptom_abdomen_vomitting_frequency = fields.Char(string="Frequency")
    symptom_abdomen_vomitting_colour = fields.Char(string="Colour")
    symptom_abdomen_vomitting_projectile = fields.Boolean(string="Projectile")
    symptom_abdomen_vomitting_bilious = fields.Boolean(string="Bilious")
    symptom_abdomen_vomitting_feculent = fields.Char(string="Feculent")
    symptom_abdomen_haematemesis = fields.Boolean(string="Haematemesis")
    symptom_abdomen_dysphagia = fields.Boolean(string="Dysphagia")
    symptom_abdomen_indigestion = fields.Boolean(string="Indigestion")
    symptom_abdomen_dyspepsia = fields.Boolean(string="Dyspepsia")
    symptom_abdomen_reflux = fields.Boolean(string="Reflux")

    symptom_abdomen_diarrhea_frequency = fields.Char(string="Frequency")
    symptom_abdomen_diarrhea_Watery = fields.Boolean(string="Watery")
    symptom_abdomen_diarrhea_mucoid = fields.Boolean(string="Mucoid")
    symptom_abdomen_diarrhea_bloody = fields.Boolean(string="Bloody")
    symptom_abdomen_diarrhea_tarry = fields.Boolean(string="Tarry")
    symptom_abdomen_diarrhea_foul_smelling = fields.Boolean(string="Foul smelling")

    symptom_abdomen_constipation = fields.Boolean(string="Constipation")
    symptom_abdomen_obstipation = fields.Boolean(string="Obstipation")
    symptom_abdomen_alternating = fields.Boolean(string="Alternating constipation and diarrhea")
    symptom_abdomen_tenesmus = fields.Boolean(string="Tenesmus")
    symptom_abdomen_borborygmi = fields.Boolean(string="Borborygmi")
    symptom_abdomen_haematochezia = fields.Boolean(string="Haematochezia")
    symptom_abdomen_pale_bulky_stools = fields.Boolean(string="Pale bulky stools")
    symptom_abdomen_appetite_gain = fields.Boolean(string="Appetite gain")
    symptom_abdomen_appetite_loss = fields.Boolean(string="Appetite loss")
    symptom_abdomen_early_satiety = fields.Boolean(string="Early satiety")
    symptom_abdomen_jaundice = fields.Boolean(string="Jaundice")
    symptom_abdomen_blood_in_stool = fields.Selection([('before stool','before stool'),('mixed with stool','mixed with stool'),
    ('after stool','after stool')],'Blood in stool')
    symptom_abdomen_others = fields.Text(string="Others")

    sign_abdomen_flat = fields.Boolean(string="Flat")
    sign_abdomen_scaphoid = fields.Boolean(string="Scaphoid")
    sign_abdomen_full = fields.Boolean(string="Full")
    sign_abdomen_distended = fields.Boolean(string="Distended")
    sign_abdomen_scarification_marks = fields.Boolean(string="Scarification marks")
    sign_abdomen_umbilical_fullness = fields.Boolean(string="Umbilical fullness")
    sign_abdomen_distended_veins = fields.Boolean(string="Distended veins")
    sign_abdomen_surgical_scar = fields.Char(string="Surgical scar")
    sign_abdomen_visible_bowel_movement = fields.Boolean(string="Visible bowel movement")
    sign_abdomen_intact_hernial_orifices = fields.Boolean(string="Intact hernial orifices")
    sign_abdomen_hernia = fields.Char(string="Hernia")
    sign_abdomen_gravid_tenderness = fields.Selection([('LH','LH'),('epigastric','epigastric'),('RH','RH'),
    ('RI','RI'),('umbilical','umbilical'),('LI','LI'),('LL','LL'),('suprapubic','suprapubic'),
    ('RL','RL')],'Gravid Tenderness')
    sign_abdomen_rebound_tenderness = fields.Boolean(string="Rebound Tenderness")
    sign_abdomen_liver = fields.Selection([('Hepatomegaly','Hepatomegaly'),('Tender liver','Tender liver'),
    ('Smooth liver','Smooth liver'),('Rough liver','Rough liver')],'Liver')
    sign_abdomen_spleen = fields.Selection([('normal','normal'),('tender','tender'),('enlarged','enlarged')],'Spleen')
    sign_abdomen_kidneys = fields.Selection([('normal','normal'),('enlarged','enlarged')],'Kidneys')
    sign_abdomen_renal_angle = fields.Selection([('right ','right '),('left','left')],'Renal angle tenderness')
    sign_abdomen_kidney_enlargement = fields.Selection([('right','right'),('left','left')],'Kidney enlargement')

    sign_abdomen_abdominal_location = fields.Char(string="Location")
    sign_abdomen_abdominal_size = fields.Char(string="Size")
    sign_abdomen_abdominal_tenderness = fields.Selection([('Tender','Tender'),('non-tender','non-tender')],'Tenderness')
    sign_abdomen_abdominal_definition = fields.Selection([('Well-defined','Well-defined'),('Attached','Attached')],'Definition')
    sign_abdomen_abdominal_texture = fields.Selection([('Smooth','Smooth'),('Irregular','Irregular')],'Texture')
    sign_abdomen_abdominal_pulsatile = fields.Selection([('Pulsatile','Pulsatile'),('Non-pulsatile','Non-pulsatile')],'Pulsatile')

    sign_abdomen_ascites = fields.Boolean(string="Ascites")
    sign_abdomen_bowel_sounds = fields.Selection([('normal','normal'),('absent','absent'),
    ('hypoactive','hypoactive'),('hyperactive','hyperactive')],'Bowel sounds')
    sign_abdomen_perianal_hygiene = fields.Selection([('good','good'),('fair','fair'),('bad','bad')],'Perianal hygiene')
    sign_sphincteric_tone = fields.Selection([('good','good'),('fair','fair'),('bad','bad')],'Sphincteric tone')
    sign_abdomen_haemorrhoids = fields.Char(string="Haemorrhoids")
    sign_abdomen_anal_fissure = fields.Char(string="Anal fissure")
    sign_abdomen_fistula_in_ano = fields.Char(string="Fistula-in-ano")
    sign_abdomen_prostate = fields.Selection([('normal','normal'),('palpable','palpable'),
    ('enlarged','enlarged'),('smooth','smooth'),('rough','rough')],'Prostate')
    sign_abdomen_rectal_mass_palpble = fields.Boolean(string="Rectal mass palpable")
    sign_abdomen_inspissated_feces_palpable = fields.Boolean(string="Inspissated feces palpable")
    sign_abdomen_examined_finger_stain = fields.Selection([('stools','stools'),('blood','blood'),
    ('mucus','mucus')],'Examining finger stained with')
    sign_abdomen_others = fields.Text(string="Others")

    # Ear, Nose & Throat
    symptom_ent_ear_discharge = fields.Selection([('right','right'),('left','left'),('serous','serous'),
    ('purulent','purulent'),('bloody','bloody')],'Ear discharge')
    symptom_ent_ear_pain = fields.Selection([('right','right'),('left','left')],'Ear pain')
    symptom_ent_ear_hearing_loss = fields.Selection([('left','left'),('right','right')],'Hearing loss')
    symptom_ent_ear_tinnitus = fields.Selection([('left','left'),('right','right')],'Tinnitus')
    symptom_ent_vertigo = fields.Boolean(string="Vertigo")
    symptom_ent_epistaxis = fields.Boolean(string="Epistaxis")
    symptom_ent_neck_swelling = fields.Char(string="Neck swelling")
    symptom_ent_neck_lump = fields.Boolean(string="Neck lump")
    symptom_ent_choking = fields.Boolean(string="Choking")
    symptom_ent_hoarseness = fields.Char(string="Hoarseness")
    symptom_ent_others = fields.Text(string="Others")

    sign_ent_auricular_lymph = fields.Char(string="Auricular lymphadenopathy")
    sign_ent_ear_discharge = fields.Selection([('serous','serous'),('bloody','bloody'),
    ('purulent','purulent')],'Ear discharge')
    sign_ent_tragal_tenderness = fields.Selection([('left','left'),('right','right')],'Tragal tenderness')
    sign_ent_describe_tympanum = fields.Char(string="Describe tympanum")
    sign_ent_rinne_test_left_ear = fields.Selection([('AC>BC','AC>BC'),('BC>AC','BC>AC')],'Left ear')
    sign_ent_rinne_test_right_ear = fields.Selection([('AC>BC','AC>BC'),('BC>AC','BC>AC')],'Right ear')
    sign_ent_weber_test = fields.Selection([('Lateralizes to right','Lateralizes to right'),('lateralizes to left','lateralizes to left')],'Weber test')
    sign_ent_neck_mass_position = fields.Selection([('Anterior','Anterior'),('Right','Right'),('Left','Left')],'Position')
    sign_ent_neck_mass_tender = fields.Selection([('Tender','Tender'),('non-tender','non-tender')],'Tender')
    sign_ent_neck_mass_temperature = fields.Selection([('Warm','Warm'),('Normal','Normal'),('Cold','Cold')],'Temperature')
    sign_ent_neck_mass_texture = fields.Selection([('Rough','Rough'),('Smooth','Smooth')],'Texture')
    sign_ent_neck_mass_pulsatile = fields.Selection([('Pulsatile','Pulsatile'),('Non-pulsatile','Non-pulsatile')],'Pulsatile')
    sign_ent_others = fields.Text(string="Others")
    
    # Genitourinary system
    symptom_genitourinary_dysuria = fields.Boolean(string="Dysuria")
    symptom_genitourinary_foul_smelling_urine = fields.Boolean(string="Foul-smelling urine")
    symptom_genitourinary_increased_frequency = fields.Boolean(string="Increased frequency")
    symptom_genitourinary_hesitancy = fields.Boolean(string="Hesitancy")
    symptom_genitourinary_weak_stream = fields.Boolean(string="Weak stream")
    symptom_genitourinary_intermittency = fields.Boolean(string="Intermittency")
    symptom_genitourinary_terminal_dribbling = fields.Boolean(string="Terminal dribbling")
    symptom_genitourinary_urgency = fields.Boolean(string="Urgency")
    symptom_genitourinary_urge_incontinence = fields.Boolean(string="Urge incontinence")
    symptom_genitourinary_straining = fields.Boolean(string="Straining")
    symptom_genitourinary_nocturia = fields.Boolean(string="Nocturia")
    symptom_genitourinary_haematuria = fields.Selection([('initial','initial'),('total','total'),
    ('terminal','terminal')],'Haematuria')
    symptom_genitourinary_splitting_urinary_stream = fields.Boolean(string="Splitting of urinary stream")
    symptom_genitourinary_pyuria = fields.Boolean(string="Pyuria")
    symptom_genitourinary_genital_discharge = fields.Selection([('white','white'),('yellow','yellow'),
    ('red','red'),('foul smelling','foul smelling')],'Genital discharge')    
    symptom_genitourinary_genital_itching = fields.Boolean(string="Genital itching")
    symptom_genitourinary_bleeding = fields.Boolean(string="Genital bleeding")
    symptom_genitourinary_others = fields.Text(string="Others")

    sign_genitourinary_normal_genitalia = fields.Boolean(string="Normal genitalia") 
    sign_genitourinary_inflammation = fields.Boolean(string="Inflammation")
    sign_genitourinary_circumcision = fields.Selection([('circumcised','circumcised'),('uncircumcised','uncircumcised')],'Circumcision')
    sign_genitourinary_genital_cutting = fields.Boolean(string="Genital cutting")
    sign_genitourinary_meatus = fields.Selection([('tip','tip'),('ventral','ventral'),('dorsal','dorsal')],'Meatus')
    sign_genitourinary_urethral_induration = fields.Boolean(string="Urethral induration")
    sign_genitourinary_chordee = fields.Selection([('ventral','ventral'),('dorsal','dorsal')],'Chordee')
    sign_genitourinary_perineal_rashes = fields.Boolean(string="Perineal rashes")
    sign_genitourinary_genital_sores = fields.Boolean(string="Genital sores")
    sign_genitourinary_ambiguous_genitalia = fields.Boolean(string="Ambiguous genitalia")
    sign_genitourinary_scrotum = fields.Selection([('Normal','Normal'),('Swollen','Swollen')],'Scrotum')
    sign_genitourinary_cervical_excitatory_tenderness = fields.Boolean(string="Cervical excitatory tenderness")
    sign_genitourinary_palpable_testes = fields.Selection([('right','right'),('left','left')],'Palpable testes')
    sign_genitourinary_hydrocele = fields.Boolean(string="Hydrocele")
    sign_genitourinary_varicocele = fields.Boolean(string="Varicocele")
    sign_genitourinary_others = fields.Text(string="Others")

    # Psychiatry
    symptom_psychiatry_low_mood = fields.Boolean(string="Low mood")
    symptom_psychiatry_mania = fields.Boolean(string="Mania")
    symptom_psychiatry_mood_swings = fields.Boolean(string="Mood swings")
    symptom_psychiatry_hallucinations = fields.Selection([('visual','visual'),('auditory','auditory'),('sensory','sensory')],'Hallucinations')
    symptom_psychiatry_delusions = fields.Selection([('love','love'),('grandiosity','grandiosity'),('persecutory','persecutory')],'Delusions')
    symptom_psychiatry_delusions_others = fields.Text(string="others")
    symptom_psychiatry_anhedonia = fields.Boolean(string="Anhedonia")
    symptom_psychiatry_insomnia_duration = fields.Char(string="Duration")
    symptom_psychiatry_insomnia_quality = fields.Char(string="Quality")
    symptom_psychiatry_hypersomnolence = fields.Boolean(string="Hypersomnolence")
    symptom_psychiatry_anxiety = fields.Boolean(string="Anxiety")
    symptom_psychiatry_phobia = fields.Char(string="Phobia")
    symptom_psychiatry_suicidal_ideations = fields.Boolean(string="Suicidal ideations")
    symptom_psychiatry_obsessions = fields.Boolean(string="Obsessions")
    symptom_psychiatry_compulsions = fields.Boolean(string="Compulsions")
    symptom_psychiatry_anorexia = fields.Boolean(string="Anorexia")
    symptom_psychiatry_bulimia = fields.Boolean(string="Bulimia")
    symptom_psychiatry_thoughts = fields.Selection([('insertion','insertion'),('broadcast','broadcast'),('deletion','deletion')],'Thoughts')
    symptom_psychiatry_libido = fields.Selection([('same','same'),('increased','increased'),('reduced','reduced')],'Libido')
    symptom_psychiatry_guilt = fields.Boolean(string="Guilt")
    symptom_psychiatry_others = fields.Boolean(string="Others")

    sign_psychiatry_oriented = fields.Boolean(string="Oriented")
    sign_psychiatry_abnormal_behaviour = fields.Boolean(string="Abnormal behaviour")
    sign_psychiatry_mood = fields.Selection([('depressed','depressed'),('manic','manic')],'Mood')
    sign_psychiatry_short_term_memory = fields.Char(string="Short term memory")
    sign_psychiatry_long_term_memory = fields.Char(string="Long term memory")
    sign_psychiatry_concentration = fields.Char(string="Concentration")
    sign_psychiatry_thought = fields.Selection([('pressure','pressure'),('poverty','poverty'),
    ('tangential thinking','tangential thinking'),('flight of ideas','flight of ideas'),('titubation','titubation')],'Thought')
    sign_psychiatry_tics = fields.Boolean(string="Tics")
    sign_psychiatry_others = fields.Text(string="Others")

    # Past medical history
    past_medical_history_sickle_cell = fields.Boolean(string="Sickle cell")
    past_medical_history_diabetes = fields.Boolean(string="Diabetes")
    past_medical_history_hypertension = fields.Boolean(string="Hypertension")
    past_medical_history_epilepsy = fields.Boolean(string="Epilepsy")
    past_medical_history_dyslipidemia = fields.Boolean(string="Dyslipidemia")
    past_medical_history_tia = fields.Boolean(string="TIA")
    past_medical_history_stroke = fields.Boolean(string="Stroke")
    past_medical_history_myocardial_infarction = fields.Boolean(string="Myocardial Infarction")
    past_medical_history_dvt = fields.Boolean(string="DVT")
    past_medical_history_surgeries = fields.Text(string="Surgeries")
    past_medical_history_asthma = fields.Boolean(string="Asthma")
    past_medical_history_copd = fields.Boolean(string="COPD")
    past_medical_history_immunization = fields.Selection([('fully','fully'),('not up-to-date','not up-to-date'),
    ('unimmunized','unimmunized')],'Immunization')
    past_medical_history_developmental_milestones = fields.Selection([('normal','normal'),('delayed','delayed')],'Developmental milestones')
    past_medical_history_others = fields.Text(string="Others")

    # Lifestyle
    lifestyle_alcohol = fields.Selection([('No','No'),('Yes','Yes')],'Alcohol')
    lifestyle_alcohol_yes = fields.Char(string="If Yes")
    lifestyle_tobacco = fields.Selection([('No','No'),('Yes','Yes')],'Tobacco')
    lifestyle_tobacco_yes = fields.Char(string="If Yes")
    lifestyle_recreational_drugs = fields.Selection([('No','No'),('Yes','Yes')],'Recreational drugs')
    lifestyle_recreational_drugs_yes = fields.Char(string="If Yes")
    lifestyle_sex = fields.Selection([('safe','safe'),('unsafe','unsafe')],'Sex')
    lifestyle_coffee = fields.Selection([('No','No'),('Yes','Yes')],'Coffee')
    lifestyle_coffee_yes = fields.Char(string="If Yes")
    lifestyle_other_risky_behaviour = fields.Text(string="Other risky behaviours")
    lifestyle_strict_vegetarian = fields.Selection([('No','No'),('Yes','Yes')],'Strict vegetarian')
    lifestyle_exercise = fields.Selection([('No','No'),('Yes','Yes')],'Exercise')
    lifestyle_exercise_yes = fields.Char(string="If Yes")

    # Medication history
    medication_history_current_medications = fields.One2many('oeha.currentmedication','evaluation_id',string="Current Medications")
    medication_history_drug_allergies = fields.Text(string="Drug allergies")

    # Gynaecological history
    gynaecology_last_menses = fields.Date(string="Last menses")
    gynaecology_amenorrhea = fields.Selection([('primary','primary'),('secondary','secondary')],'Amenorrhea')
    gynaecology_dysmenorrhea = fields.Boolean(string="Dysmenorrhea")
    gynaecology_menorrhagia = fields.Boolean(string="Menorrhagia")
    gynaecology_metromenorrhagia = fields.Boolean(string="Metromenorrhagia")
    gynaecology_infertility = fields.Selection([('primary','primary'),('secondary','secondary')],'Infertility')
    gynaecology_subfertility = fields.Boolean(string="Subfertility")

    # Family history
    family_history_condition = fields.Text(string="Condition")

    # Nursing Assessment
    # Nutrition
    diet = fields.Selection( [('regular', 'Regular'), ('soft', 'Soft'),('pureed', 'Pureed')],'Diet')
    recent_weight_change = fields.Boolean(string="Recent weight Change")
    conditions_affecting_ecs = fields.Boolean(string="Condition affecting eating, chewing and swallowing")    
    mucous_membranes = fields.Selection( [('moist', 'Moist'), ('dry', 'Dry')],'Mucous Membranes')    

    # skin
    skin = fields.Selection( [('normal', 'Normal'), ('pale', 'Pale'),('red', 'Red'),
    ('rash', 'Rash'),('bruise','Bruise'),('breakdown','Skinbreakdown')],'Skin')
    skin_intact = fields.Boolean(string="Skin intact")
    special_care = fields.Boolean(string="Special care required")
    wound_assessment = fields.Text(string='Wound Assessment', required=False)

    # neuro
    level_of_consciousness = fields.Selection( [('alert', 'Alert'), ('altered', 'Altered')],'Level of consciousness')
    seizure_tremor_fainting = fields.Boolean(string="seizure / tremor / fainting")
    difficulty_in_orientation = fields.Boolean(string="Difficulty in orientation")
    sensation = fields.Selection( [('intact', 'Intact'), ('diminished', 'Diminished'), ('absent', 'Absent')],'Intact / Diminished / Absent')
    memory_deficit = fields.Boolean(string="Memory Deficit")
    impaired_decision_making = fields.Boolean(string="Impaired decision making")
    sleep_aids = fields.Boolean(string="Sleep aids")

    # pain / discomfort
    pain = fields.Boolean(string="Pain")
    pain_score = fields.Selection( [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    , (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')],'Pain Score')
    location = fields.Char(string='Location')
    frequency = fields.Char(string='Frequency')
    duration = fields.Char(string='Duration')
    treatment = fields.Char(string='Treatment (if any)')

    # respiration
    respirations = fields.Selection( [('regular', 'Regular'), ('unlabored', 'Unlabored'),
     ('irregular', 'Irregular'), ('labored', 'Labored')],'Respirations')
    breath_sounds = fields.Selection( [('clear', 'Clear'), ('wheezes', 'Wheezes'),('crackles','Crackles')],'Breath sounds')
    shorthess_of_breath = fields.Boolean(string="Shortness of breath")
    shorthess_of_breath_trigger = fields.Text('Trigger')
    cough = fields.Boolean(string="Cough")
    cough_type = fields.Selection( [('productive', 'Productive'), ('non_productive', 'Non Productive')],
    'Productive / Non Productive')
    respiratory_treatment = fields.Selection( [('none', 'None'), ('oxygen', 'Oxygen'),
    ('nebulizer','Nebulizer'),('cpap','CPAP'),('bipap','BIPAP')],'Respiratory Treatments')

    # cardiovascular / circulation
    history = fields.Selection( [('normal', 'Normal'), ('arrythmia', 'Arrythmia'),
    ('hypertension','Hypotension'),('dizziness','Dizziness')],'History')
    pulse = fields.Selection( [('regular', 'Regular'), ('irregular', 'Irregular')],'Pulse')
    edema = fields.Boolean(string="Edema")
    explain_edema = fields.Text('Explain edema if any')
    chest_pain = fields.Boolean(string="Chest pain")
    explain_chest_pain = fields.Text('Explain chest pain if any')

    # gastro intestinal
    gastrointestinal_bleeding = fields.Boolean(string="Bleeding")
    gastrointestinal_diarrhea = fields.Boolean(string="Diarrhea")
    gastrointestinal_constipation = fields.Boolean(string="Constipation")
    gastrointestinal_vomiting = fields.Boolean(string="Vomiting")
    gastrointestinal_nausea = fields.Boolean(string="Nausea")
    gastrointestinal_gastrostomy = fields.Boolean(string="Gastrostomy")
    gastrointestinal_enteral_tube = fields.Boolean(string="Enteral tube")
    gastrointestinal_abdominal_pain = fields.Boolean(string="Abdominal Pain")

    change_in_appetite = fields.Selection( [('yes', 'Yes'), ('no', 'No')],'Change in appetite')
    explain_change_in_appetite = fields.Text('Explain change in appetite')
    bowel_sounds = fields.Boolean(string="Bowel sounds")
    bowel_movement = fields.Boolean(string="Bowel movement")

    # genitourinary
    bladder_control = fields.Selection( [('full_control', 'Full Control'),
     ('incontinence', 'Incontinence')],'Bladder Control')
    bladder_frequency = fields.Char(string='Frequency')
    blood_in_urine = fields.Boolean(string="Blood in urine")
    difficulty_urinating = fields.Boolean(string="Difficulty urinating")
    nocturnia = fields.Boolean(string="Nocturnia")
    indwelling_catheter = fields.Boolean(string="Indwelling catheter")

    # musculoskeletal
    mobility = fields.Selection( [('normal', 'Normal'), ('impaired', 'Impaired')],'Mobility')
    assistive_devices = fields.Boolean(string="Assistive devices")
    range_of_motion = fields.Selection( [('full', 'Full'), ('limited', 'Limited')],'Range of motion')
    activities_of_daily = fields.Selection( [('self', 'Self'), ('assist', 'Assit'),
    ('total','Total')],'Activities of daily living')

    # sensory
    vision = fields.Selection( [('normal', 'Normal'), ('impaired', 'Impaired')],'Vision')
    corrective_device = fields.Char('Corrective device')
    hearing = fields.Selection( [('normal', 'Normal'), ('impaired', 'Impaired')],'Hearing')
    hearing_aid = fields.Boolean(string="Hearing Aid")

    # nursing assessment notes
    nursing_assessment_notes = fields.Text(string="Notes")
    ####################################################################
    # current medications
    allergies = fields.Boolean('Allergies')
    allergy_cause = fields.Text(string="Cause of Allergy")
    allergic_reaction_seen = fields.Text(string="Allergic reaction seen")
    current_medication = fields.Selection( [('yes', 'Yes'), ('no', 'No')],'Any current medications?')
    currentmedications = fields.One2many('oeha.currentmedication','evaluation_id',string="Current Medications")
    other_medications = fields.Text(string="Other medications")

    #######################################################################
    # Treatment sheet
    treatments_administered = fields.One2many('oeha.treatmentmedication','evaluation_id',string="Medications Administered")
    procedures_performed = fields.One2many('oeha.treatmentprocedure','evaluation_id',string="Treatments / Procedures Performed")
    iv_procedures_performed = fields.One2many('oeha.ivprocedure','evaluation_id',string="IV Procedures Performed") 

    # Discharge summary
    discharge_patient_name = fields.Char(string="Patient Name", related='patient.name',readonly=True)
    discharge_patient_id = fields.Char(string="Patient ID", related='patient.identification_code',readonly=True)
    patient_admission_date = fields.Date(string="Admission Date")
    patient_discharge_date = fields.Date('Discharge Date')
    discharge_attending_physician = fields.Char(string="Attending Physician", related='doctor.name', readonly=True)
    discharge_admission_diagnosis = fields.Char(string="Admission Diagnosis",related='indication.name',readonly=True)
    discharge_final_diagnoses = fields.Many2one('oeh.medical.pathology', string='Final Diagnoses')
    discharge_condition = fields.Text(string="Condition on discharge")
    
    present_illness_history = fields.Text(string="History of present illness")
    discharge_medications = fields.One2many('oeha.dischargemedication','evaluation_id',string="Discharge Medications")
    discharge_procedures = fields.One2many('oeha.dischargeprocedure','evaluation_id',string="Discharge Treatments / Procedures Performed")
    discharge_instructions = fields.Text(string="Discharge Instructions")
    discharge_completed_by = fields.Many2one('res.users','Completed By', default=lambda self: self.env.user)
    
    #Doctor Edit Function
    can_edit = fields.Boolean(string='Edit')

    # Evaluation addedndum
    evaluation_addendum = fields.Text(string="Evaluation addendum")


# List of current medications
class CurrentMedications(models.Model):
    _name = 'oeha.currentmedication'
    _description = 'Current medications'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Many2one('oeh.medical.medicines', string='Medication')
    start_date = fields.Date(string="Start date")
    dose = fields.Integer(string='Dose', help="Amount of medicines (eg, 250 mg ) each time the patient takes it")
    dose_unit = fields.Many2one('oeh.medical.dose.unit', string='Dose Unit', help="Unit of measure for the medication to be taken")
    dose_form = fields.Many2one('oeh.medical.drug.form','Form', help="Drug form, such as tablet or gel")
    qty = fields.Integer(string='x', help="Quantity of units (eg, 2 capsules) of the medicament", default=lambda *a: 1.0)
    route = fields.Many2one('oeh.medical.drug.route', 'Route')
    frequency = fields.Many2one('oeh.medical.dosage', 'Frequency')


# Treatment sheet medications
class TreatmentMedications(models.Model):
    _name = 'oeha.treatmentmedication'
    _description = 'Medications administered'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Many2one('oeh.medical.medicines',string='Medication')
    dose = fields.Integer(string='Dose', help="Amount of medicines (eg, 250 mg ) each time the patient takes it")
    dose_unit = fields.Many2one('oeh.medical.dose.unit', string='Dose Unit', help="Unit of measure for the medication to be taken")
    dose_form = fields.Many2one('oeh.medical.drug.form','Form', help="Drug form, such as tablet or gel")
    qty = fields.Integer(string='x', help="Quantity of units (eg, 2 capsules) of the medicament", default=lambda *a: 1.0)
    route = fields.Many2one('oeh.medical.drug.route', 'Route')
    time = fields.Datetime('Date and Time')
    administered_by = fields.Many2one('res.users','Administered By', default=lambda self: self.env.user)
    comments = fields.Text(string="Comments")


# Treatment sheet procedures
class TreatmentProcedure(models.Model):
    _name = 'oeha.treatmentprocedure'
    _description = 'Treatment procedure administered'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Many2one('oeh.medical.procedure',string='Procedure')
    site = fields.Char(string="Site")
    time = fields.Datetime(string="Date / Time")
    performed_by = fields.Many2one('res.users','Performed By', default=lambda self: self.env.user)
    comments = fields.Text(string="Comments")

class DischargeMedications(models.Model):
    _name = 'oeha.dischargemedication'
    _description = 'Discharge medications'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Many2one('oeh.medical.medicines',string='Medication')
    dose = fields.Integer(string='Dose', help="Amount of medicines (eg, 250 mg ) each time the patient takes it")
    dose_unit = fields.Many2one('oeh.medical.dose.unit', string='Dose Unit', help="Unit of measure for the medication to be taken")
    dose_form = fields.Many2one('oeh.medical.drug.form','Form', help="Drug form, such as tablet or gel")
    qty = fields.Integer(string='x', help="Quantity of units (eg, 2 capsules) of the medicament", default=lambda *a: 1.0)
    route = fields.Many2one('oeh.medical.drug.route', 'Route')
    time = fields.Datetime('Date and Time')
    administered_by = fields.Many2one('res.users','Administered By', default=lambda self: self.env.user)
    comments = fields.Text(string="Comments")


# Treatment sheet procedures
class DischargeProcedure(models.Model):
    _name = 'oeha.dischargeprocedure'
    _description = 'Discharge Procedures'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Many2one('oeh.medical.procedure',string='Procedure')
    site = fields.Char(string="Site")
    time = fields.Datetime(string="Date / Time")
    performed_by = fields.Many2one('res.users','Performed By', default=lambda self: self.env.user)
    comments = fields.Text(string="Comments")


# Treatment sheet procedures
class IVProcedure(models.Model):
    _name = 'oeha.ivprocedure'
    _description = 'IV Procedures'

    evaluation_id = fields.Many2one('oeh.medical.evaluation', string='Evaluation Reference', required=True, ondelete='cascade', index=True)
    name = fields.Char(string='Procedure')
    needle_size = fields.Integer(string='Needle size (mm)')
    site = fields.Char(string="Site")
    fluid_type = fields.Char(string='Type of fluids / ml')
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    performed_by = fields.Many2one('res.users','Performed By', default=lambda self: self.env.user)
    comments = fields.Text(string="Comments")



