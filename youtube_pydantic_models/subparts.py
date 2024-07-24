from pydantic import BaseModel, Field
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)


class SharedContentStream(BaseModel):
    model_config = get_base_model_config()

    channel_count: int | None = Field(default=None)
    codec: str | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    vendor: str | None = Field(default=None)


class AudioStream(SharedContentStream):
    model_config = get_base_model_config()

    channel_count: int | None = Field(default=None)


class VideoStream(SharedContentStream):
    model_config = get_base_model_config()

    width_pixels: int | None = Field(default=None)
    height_pixels: int | None = Field(default=None)
    frame_rate_fps: float | None = Field(default=None)
    aspect_ratio: float | None = Field(default=None)
    rotation: str | None = Field(default=None)


class Channel(BaseModel):
    model_config = get_base_model_config()

    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    keywords: str | None = Field(default=None)
    tracking_analytics_account_id: str | None = Field(default=None)
    unsubscribed_trailer: str | None = Field(default=None)
    country: str | None = Field(default=None)
    default_language: str | None = Field(default=None)


class ContentRating(BaseModel):
    model_config = get_base_model_config()

    acb_rating: str | None = Field(default=None)
    agcom_rating: str | None = Field(default=None)
    anatel_rating: str | None = Field(default=None)
    bbfc_rating: str | None = Field(default=None)
    bfvc_rating: str | None = Field(default=None)
    bmukk_rating: str | None = Field(default=None)
    catv_rating: str | None = Field(default=None)
    catvfr_rating: str | None = Field(default=None)
    cbfc_rating: str | None = Field(default=None)
    ccc_rating: str | None = Field(default=None)
    cce_rating: str | None = Field(default=None)
    chfilm_rating: str | None = Field(default=None)
    chvrs_rating: str | None = Field(default=None)
    cicf_rating: str | None = Field(default=None)
    cna_rating: str | None = Field(default=None)
    cnc_rating: str | None = Field(default=None)
    csa_rating: str | None = Field(default=None)
    cscf_rating: str | None = Field(default=None)
    czfilm_rating: str | None = Field(default=None)
    djctq_rating: str | None = Field(default=None)
    djctq_rating_reasons: list[str] | None = Field(default=None)
    ecbmct_rating: str | None = Field(default=None)
    eefilm_rating: str | None = Field(default=None)
    egfilm_rating: str | None = Field(default=None)
    eirin_rating: str | None = Field(default=None)
    fcbm_rating: str | None = Field(default=None)
    fco_rating: str | None = Field(default=None)
    fmoc_rating: str | None = Field(default=None)
    fpb_rating: str | None = Field(default=None)
    fpb_rating_reasons: list[str] | None = Field(default=None)
    fsk_rating: str | None = Field(default=None)
    grfilm_rating: str | None = Field(default=None)
    icaa_rating: str | None = Field(default=None)
    ifco_rating: str | None = Field(default=None)
    ilfilm_rating: str | None = Field(default=None)
    incaa_rating: str | None = Field(default=None)
    kfcb_rating: str | None = Field(default=None)
    kijkwijzer_rating: str | None = Field(default=None)
    kmrb_rating: str | None = Field(default=None)
    lsf_rating: str | None = Field(default=None)
    mccaa_rating: str | None = Field(default=None)
    mccyp_rating: str | None = Field(default=None)
    mcst_rating: str | None = Field(default=None)
    mda_rating: str | None = Field(default=None)
    medietilsynet_rating: str | None = Field(default=None)
    meku_rating: str | None = Field(default=None)
    mibac_rating: str | None = Field(default=None)
    moc_rating: str | None = Field(default=None)
    moctw_rating: str | None = Field(default=None)
    mpaa_rating: str | None = Field(default=None)
    mpaat_rating: str | None = Field(default=None)
    mtrcb_rating: str | None = Field(default=None)
    nbc_rating: str | None = Field(default=None)
    nbcpl_rating: str | None = Field(default=None)
    nfrc_rating: str | None = Field(default=None)
    nfvcb_rating: str | None = Field(default=None)
    nkclv_rating: str | None = Field(default=None)
    oflc_rating: str | None = Field(default=None)
    pefilm_rating: str | None = Field(default=None)
    rcnof_rating: str | None = Field(default=None)
    resorteviolencia_rating: str | None = Field(default=None)
    rtc_rating: str | None = Field(default=None)
    rte_rating: str | None = Field(default=None)
    russia_rating: str | None = Field(default=None)
    skfilm_rating: str | None = Field(default=None)
    smais_rating: str | None = Field(default=None)
    smsa_rating: str | None = Field(default=None)
    tvpg_rating: str | None = Field(default=None)
    yt_rating: str | None = Field(default=None)


class Image(BaseModel):
    model_config = get_base_model_config()

    banner_external_url: str | None = Field(default=None)


class Localization(BaseModel):
    model_config = get_base_model_config()

    title: str | None = Field(default=None)
    description: str | None = Field(default=None)


class Localized(BaseModel):
    model_config = get_base_model_config()
    
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)


class ProcessingProgress(BaseModel):
    model_config = get_base_model_config()

    parts_total: int | None = Field(default=None)
    parts_processed: int | None = Field(default=None)
    time_left_ms: int | None = Field(default=None)


class RegionRestriction(BaseModel):
    model_config = get_base_model_config()

    allowed: list[str] | None = Field(default=None)
    blocked: list[str] | None = Field(default=None)


class RelatedPlaylists(BaseModel):
    model_config = get_base_model_config()

    likes: str | None = Field(default=None)
    uploads: str | None = Field(default=None)
    favorites: str | None = Field(default=None)


class TagSuggestions(BaseModel):
    model_config = get_base_model_config()

    tag: str | None = Field(default=None)
    category_restricts: list[str] | None = Field(default=None)


class Thumbnail(BaseModel):
    model_config = get_base_model_config()
    
    url: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)


class Watch(BaseModel):
    model_config = get_base_model_config()

    text_color: str | None = Field(default=None)
    background_color: str | None = Field(default=None)
    featured_playlist_id: str | None = Field(default=None)
